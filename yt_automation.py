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
