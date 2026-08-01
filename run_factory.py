import os
import glob
from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip, TextClip

def build_video():
    audio_path = "voice.mp3"
    caption_path = "caption.txt"
    output_path = "output.mp4"

    if not os.path.exists(audio_path):
        print("❌ File voice.mp3 tidak ditemukan!")
        return

    # Load audio
    audio = AudioFileClip(audio_path)
    duration = audio.duration

    # Read caption
    caption_text = "Video Terbaru"
    if os.path.exists(caption_path):
        with open(caption_path, "r", encoding="utf-8") as f:
            caption_text = f.read().strip()

    # Background Canvas Vertikal (1080x1920)
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15), duration=duration)

    # Render video
    video = CompositeVideoClip([bg]).set_audio(audio)
    video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"✅ Video berhasil dibuat: {output_path}")

if __name__ == "__main__":
    build_video()
