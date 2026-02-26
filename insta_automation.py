# Instagram Reels Upload Automation (Instagram Graph API)
# 
# SETUP INSTRUCTIONS:
# 1. Install Facebook SDK: pip install facebook-sdk requests
# 2. Create Facebook Developer Account: https://developers.facebook.com/
# 3. Create a new app with Instagram Graph API access
# 4. Convert Instagram account to Business/Creator account
# 5. Link Instagram account to Facebook Page
# 6. Get long-lived access token from Graph API Explorer
# 7. Add to .env file:
#    INSTAGRAM_ACCESS_TOKEN=your_long_lived_token
#    INSTAGRAM_BUSINESS_ACCOUNT_ID=your_account_id
# 8. Token expires in 60 days - refresh before expiration
# 
# USAGE:
# python insta_automation.py
# 
# WORKFLOW:
# - Reads all .mp4 files from ready_to_upload/ folder
# - Creates media container with video URL (must be publicly accessible)
# - Sets caption with hashtags (#fyp #storytime #reddit)
# - Publishes container as Reel
# - Waits for processing completion before next upload
# 
# IMPORTANT NOTES:
# - Video must be hosted on public URL (use AWS S3, Cloudinary, or temporary hosting)
# - Reels requirements: 9:16 aspect ratio, 4-60 seconds, max 1GB, H.264 codec
# - Rate limits: ~25 API calls per user per hour
# - Publishing takes 30-60 seconds for Instagram to process video
# - Use IG_REELS media type for Reels (not VIDEO)
# - Cannot schedule Reels via API - only immediate publishing
# - Captions max 2200 characters, max 30 hashtags
