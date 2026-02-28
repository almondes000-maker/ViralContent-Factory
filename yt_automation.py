# YouTube Shorts Upload Automation (YouTube Data API v3)
# 
# SETUP INSTRUCTIONS:
# 1. Install Google API Client: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# 2. Go to Google Cloud Console: https://console.cloud.google.com/
# 3. Create a new project or select existing one
# 4. Enable YouTube Data API v3 for your project
# 5. Create OAuth 2.0 credentials (Desktop App)
# 6. Download client_secrets.json and place in project root
# 7. First run will open browser for OAuth consent - authorize the app
# 8. Token will be saved for future runs
# 
# USAGE:
# python yt_automation.py
# 
# WORKFLOW:
# - Reads all .mp4 files from ready_to_upload/ folder
# - Authenticates using OAuth 2.0
# - Uploads each video using videos.insert API endpoint
# - Sets title, description, tags, category (22 = People & Blogs)
# - Sets privacy status (public/private/unlisted)
# - Monitors upload progress with resumable upload
# 
# IMPORTANT NOTES:
# - YouTube Shorts are auto-detected if video is vertical (9:16) and under 60 seconds
# - Add #Shorts to title/description for better discoverability
# - Default quota: 10,000 units/day (1 upload = ~1600 units, ~6 videos/day)
# - Request quota increase if needed: https://support.google.com/youtube/contact/yt_api_form
# - Resumable uploads handle network interruptions automatically
# - Maximum file size: 256GB (128GB for unverified accounts)

import os
import json
import glob
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
script_path=os.path.dirname(os.path.abspath(__file__))
credentials_path=os.path.join(script_path,"client.json")
scripts_path=os.path.join(script_path,"scripts.json")

def get_authenticated_service():
    """Authenticate and return the YouTube API service."""
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def get_video_metadata(video_id):
    """Get metadata from scripts.json for a video ID."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script["posted"] == True:
            continue
        if script["id"] == video_id:
            return script
    return None

def mark_as_posted(video_id):
    """Saves the 'posted' status back to the physical database."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
        
    for script in scripts:
        if script["id"] == video_id:
            script["posted"] = True
            break
            
    with open(scripts_path, "w", encoding="utf-8") as f:
        json.dump(scripts, f, indent=4, ensure_ascii=False)

def upload_video(file_path, metadata):
    """Uploads a video to YouTube with metadata from scripts.json."""
    youtube = get_authenticated_service()

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    # Build title and description from metadata
    raw_hook = metadata['hook']
    if len(raw_hook) > 92:
        raw_hook = raw_hook[:89] + "..."

    title = f"{raw_hook} #Shorts"
    raw_tags = metadata["tags"]

    clean_tags=[]
    for tag in raw_tags:
        if isinstance(tag,str):
            word_count=len(tag.split())
            char_count=len(tag)
            if word_count <= 6 and char_count <= 35:
                clean_tags.append(tag)
        else:
            continue

    hashtag_string = ' '.join(['#' + tag.replace(' ', '') for tag in clean_tags])
    description = (
        f"{metadata['hook']}\n\n"
        f"Wait until you hear how this ends... 💀\n\n"
        f"Who do you think is actually in the wrong here? Let me know your thoughts in the comments! 👇\n\n"
        f"{hashtag_string} #RedditStories #StoryTime"
    )
    
    body = {
        "snippet": {
            "title": title,  # YouTube title limit
            "description": description[:5000],  # YouTube description limit
            "tags": clean_tags + ["Shorts", "YouTubeShorts", "RedditStories"],
            "categoryId": "24"  # Entertainment
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

    try:
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()
        print(f"✅ Uploaded: {metadata['id']} | Video ID: {response['id']}")
        mark_as_posted(video_id=metadata['id'])
        return True
    except HttpError as e:
        print(f"❌ Upload failed for {metadata['id']}: {e}")
        return False

if __name__ == "__main__":
    # Get all videos from ready_to_upload folder
    video_files = glob.glob("ready_to_upload/*.mp4")
    
    if not video_files:
        print("No videos found in ready_to_upload/ folder")
    else:
        print(f"Found {len(video_files)} videos to upload\n")
        
        success_count = 0
        for video_path in video_files:
            # Extract video ID from filename (format: Title_words_ID.mp4)
            filename = os.path.basename(video_path)
            video_id = filename.replace(".mp4", "").split("_")[-1]
            
            # Get metadata from scripts.json
            metadata = get_video_metadata(video_id)
            
            if metadata:
                print(f"Uploading: {filename}")
                if upload_video(video_path, metadata):
                    success_count += 1
                print()
            else:
                print(f"⚠️ No metadata found for {video_id}, skipping\n")
        
        print(f"\n{'='*50}")
        print(f"Upload complete: {success_count}/{len(video_files)} successful")

