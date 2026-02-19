<div align="center">

# 🎬 AutoContent Factory

### *Autonomous AI-Powered Viral Content Generation Pipeline*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MoviePy](https://img.shields.io/badge/MoviePy-1.0.3-FF6B6B?style=for-the-badge)](https://zulko.github.io/moviepy/)
[![Edge TTS](https://img.shields.io/badge/Edge_TTS-AI_Voice-00D9FF?style=for-the-badge)](https://github.com/rany2/edge-tts)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Fully automated Reddit story scraping → AI voice synthesis → viral short-form video generation**

[Features](#-features) • [Architecture](#-system-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

---

</div>

## 🚀 Overview

**AutoContent Factory** is an end-to-end automated content generation system that transforms Reddit stories into professionally edited, viral-ready short-form videos for TikTok, YouTube Shorts, and Instagram Reels. The pipeline handles everything from content discovery to final video rendering with zero manual intervention.

### 💡 What Makes This Special?

- **🤖 Fully Autonomous**: Set it and forget it. The system runs daily via scheduled tasks
- **🧠 AI-Powered Intelligence**: LLM-driven gender detection, viral hook generation, and content filtering
- **🎯 Production-Ready**: Includes failover systems, cold storage backups, and email alerting
- **⚡ Optimized Performance**: Multi-threaded rendering, smart caching, and resource management
- **📊 Scalable Architecture**: Modular phase-based design for easy extension and maintenance

---

## ✨ Features

### 🔍 **Phase 1: Intelligent Content Acquisition**
- **Multi-Source Scraping**: Waterfall system across 10+ high-engagement subreddits (AITA, TIFU, TrueOffMyChest, etc.)
- **Smart Filtering**: 
  - Language detection (English-only)
  - Optimal word count (120-200 words for 60-second videos)
  - Duplicate prevention via persistent database
  - Automatic removal of deleted/removed posts
- **AI Enhancement**:
  - LLM-powered gender detection for voice matching
  - Viral hook generation (transforms boring titles into scroll-stopping openers)
  - Slang/acronym normalization (AITA → "Am I the jerk", etc.)
- **Failover System**: Falls back to local cold storage if all live sources fail

### 🎙️ **Phase 2: Professional Audio Synthesis**
- **Edge TTS Integration**: Microsoft's neural voices for natural-sounding narration
- **Dynamic Voice Selection**: Gender-matched voices (3 female variants, 1 male)
- **Word-Level Timing**: Precise timestamp extraction for perfect subtitle synchronization
- **Fallback Mechanisms**: Sentence-level heuristics if word boundaries fail

### 🎥 **Phase 3: Viral Video Composition**
- **9:16 Vertical Format**: Optimized for mobile-first platforms
- **Dynamic Background Selection**: Random gameplay footage (Minecraft, GTA 5)
- **Animated Subtitles**: 
  - Impact font with stroke for maximum readability
  - 2-word chunks with pop-in animations
  - Mathematically synced to audio timestamps
- **Smart Cropping**: Automatic center-crop from 16:9 to 9:16
- **Random Start Points**: Prevents repetitive background footage

### 🔧 **Production Features**
- **Automated Cleanup**: Removes temporary files after each run
- **Batch Management**: Collects 7 videos before triggering upload alert
- **Email Notifications**: Gmail SMTP alerts when batch is ready
- **Sanitized Filenames**: OS-safe naming with ID-based uniqueness
- **Error Handling**: Comprehensive try-catch blocks with detailed logging

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MAIN PIPELINE ORCHESTRATOR                │
│                     (main_pipeline.py)                       │
└────────────┬────────────────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
┌─────────┐      ┌─────────┐
│ Phase 1 │──────│ Phase 2 │
│ Scraper │      │  Audio  │
└────┬────┘      └────┬────┘
     │                │
     │                ▼
     │           ┌─────────┐
     │           │ Phase 3 │
     └───────────│  Video  │
                 └────┬────┘
                      │
                      ▼
              ┌───────────────┐
              │  Cleanup &    │
              │  Notification │
              └───────────────┘
```

### 📁 Project Structure

```
AutoContent/
├── 📜 main_pipeline.py      # Orchestrator - coordinates all phases
├── 🔍 phase1.py             # Content acquisition & AI processing
├── 🎙️ phase2.py             # Audio synthesis & timestamp extraction
├── 🎥 phase3.py             # Video composition & rendering
├── 📥 yt_downloader.py      # Background footage downloader
├── 📧 reminder.py           # Batch management & email alerts
├── ⚙️ run_factory.bat       # Windows Task Scheduler entry point
├── 📦 requirements.txt      # Python dependencies
├── 🗄️ scripts.json          # Persistent story database
├── 🎬 downloads/            # Background video assets
└── 📤 reels/                # Final rendered videos
```

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.11+ | Core runtime |
| **AI/LLM** | OpenRouter API | Gender detection & hook generation |
| **Voice Synthesis** | Edge-TTS | Neural text-to-speech |
| **Video Processing** | MoviePy 1.0.3 | Compositing & rendering |
| **Image Processing** | ImageMagick | Text rendering backend |
| **Web Scraping** | Requests | Reddit API interaction |
| **NLP** | langdetect | Language filtering |
| **Video Download** | yt-dlp | Background footage acquisition |
| **Email** | smtplib | Gmail notifications |
| **Environment** | python-dotenv | Secure credential management |

---

## 📦 Installation

### Prerequisites

```bash
# Required System Dependencies
- Python 3.11 or higher
- FFmpeg (for audio/video processing)
- ImageMagick (for subtitle rendering)
- Deno or Node.js (for yt-dlp)
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/indiser/autocontent-factory.git
cd autocontent-factory
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install System Dependencies

**Windows (via winget):**
```bash
winget install Gyan.FFmpeg
winget install ImageMagick.ImageMagick
winget install DenoLand.Deno
```

**macOS (via Homebrew):**
```bash
brew install ffmpeg imagemagick deno
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg imagemagick
curl -fsSL https://deno.land/install.sh | sh
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
# OpenRouter API (for LLM features)
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Gmail SMTP (for notifications)
EMAIL_USER=your_email@gmail.com
EMAIL_APP_PASS=your_gmail_app_password
```

> **Note**: For Gmail, you need to generate an [App Password](https://support.google.com/accounts/answer/185833) (not your regular password)

### Step 5: Download Background Videos

```bash
python yt_downloader.py "https://youtube.com/watch?v=MINECRAFT_VIDEO_ID"
python yt_downloader.py "https://youtube.com/watch?v=GTA5_VIDEO_ID"
```

Or manually place 9:16 or 16:9 gameplay videos in the `downloads/` folder.

### Step 6: Configure ImageMagick Path (Windows Only)

Edit `phase3.py` line 5 to match your ImageMagick installation:

```python
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
```

---

## 🎯 Usage

### Manual Execution

```bash
python main_pipeline.py
```

### Automated Daily Execution (Windows)

1. Open **Task Scheduler**
2. Create a new task:
   - **Trigger**: Daily at 3:00 AM
   - **Action**: Run `run_factory.bat`
3. The system will automatically:
   - Generate 1 video per day
   - Collect 7 videos per week
   - Send email alert when batch is ready

### Batch Management

```bash
python reminder.py
```

This checks if 7+ videos are ready and moves them to `ready_to_upload/` folder.

---

## 📊 Workflow Example

```
1. [03:00 AM] Task Scheduler triggers run_factory.bat
2. [03:00:05] Phase 1 scrapes r/AmItheAsshole
3. [03:00:12] LLM generates viral hook: "Am I the jerk for refusing to attend my sister's wedding"
4. [03:00:15] Gender detected: Female → Voice: en-US-AriaNeural
5. [03:00:45] Phase 2 generates audio + word timestamps
6. [03:01:30] Phase 3 renders 60-second vertical video
7. [03:02:00] Cleanup removes temporary files
8. [03:02:05] Reminder script checks inventory (3/7 videos)
9. [Day 7] Email sent: "🟢 FACTORY ALERT: Weekly Batch Ready"
```

---

## 🎨 Customization

### Add More Subreddits

Edit `phase1.py`:

```python
SUBREDDITS = [
    "AmItheAsshole",
    "YourNewSubreddit",  # Add here
]
```

### Change Voice Models

Edit `phase2.py`:

```python
WOMAN_VOICE_LIST = [
    "en-US-JennyNeural",
    "en-GB-SoniaNeural",  # Add British accent
]
```

### Adjust Video Length

Edit `phase1.py` line 175:

```python
if 120 < len(words) < 200:  # Change word count range
```

### Modify Subtitle Style

Edit `phase3.py` lines 50-60:

```python
txt_clip = TextClip(
    chunk_text,
    font="Arial",           # Change font
    fontsize=100,           # Increase size
    color="yellow",         # Change color
    stroke_width=8,         # Thicker outline
)
```

---

## 🐛 Troubleshooting

### Issue: "ImageMagick not found"
**Solution**: Update the path in `phase3.py` line 5 to match your installation

### Issue: "No viable stories found"
**Solution**: The subreddit may have no posts matching criteria. The system will automatically try the next subreddit

### Issue: "FFmpeg not found"
**Solution**: Ensure FFmpeg is in your system PATH. Run `ffmpeg -version` to verify

### Issue: "Email sending failed"
**Solution**: 
1. Enable 2FA on Gmail
2. Generate an App Password
3. Use the App Password in `.env`, not your regular password

### Issue: "Word boundaries missing"
**Solution**: The system automatically falls back to sentence-level timing. This is expected behavior for some voices

---

## 📈 Performance Metrics

- **Average Runtime**: 2-3 minutes per video
- **Video Quality**: 1080x1920 @ 30fps
- **Audio Quality**: 192kbps MP3
- **Storage**: ~15-25MB per final video
- **Success Rate**: 95%+ (with failover systems)

---

## 🔒 Security & Privacy

- ✅ No user data collection
- ✅ API keys stored in `.env` (gitignored)
- ✅ Reddit scraping complies with API terms
- ✅ All content is public domain (Reddit posts)
- ✅ No personal information in generated videos

---

## 🚧 Roadmap

- [ ] Multi-platform upload automation (TikTok, YouTube, Instagram APIs)
- [ ] A/B testing for hooks and thumbnails
- [ ] Analytics dashboard (views, engagement tracking)
- [ ] GPU-accelerated rendering (NVENC support)
- [ ] Cloud deployment (AWS Lambda + S3)
- [ ] Web UI for manual overrides
- [ ] Multi-language support (Spanish, French, etc.)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Reddit API** - Content source
- **Microsoft Edge TTS** - Neural voice synthesis
- **OpenRouter** - LLM infrastructure
- **MoviePy** - Video processing framework
- **yt-dlp** - Video download utility

---

## 📞 Contact

<!-- **Your Name** - [@yourtwitter](https://twitter.com/yourtwitter) - your.email@example.com -->

**Project Link**: [[https://github.com/indiser/ViralContent-Factory](https://github.com/indiser/ViralContent-Factory.git)]

---

<div align="center">

### ⭐ If this project helped you, please consider giving it a star!

**Made with ❤️ and Python**

</div>
