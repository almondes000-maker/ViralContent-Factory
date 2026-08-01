import os
import requests
from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip

def download_background_image(query):
    print(f"🔍 Mencari gambar ilustrasi untuk: {query}")
    url = f"https://source.unsplash.com/1080x1920/?{requests.utils.quote(query)},mystery,story"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open("bg.jpg", "wb") as f:
                f.write(response.content)
            print("✅ Gambar ilustrasi berhasil diunduh!")
            return "bg.jpg"
    except Exception as e:
        print(f"⚠️ Gagal mengunduh gambar Unsplash: {e}")
    return None

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
    caption_text = "Sherlock Holmes Story"
    if os.path.exists(caption_path):
        with open(caption_path, "r", encoding="utf-8") as f:
            caption_text = f.read().strip()

    # Dapatkan gambar ilustrasi
    img_file = download_background_image(caption_text[:30])

    if img_file and os.path.exists(img_file):
        bg = ImageClip(img_file).set_duration(duration).resize((1080, 1920))
    else:
        # Fallback jika gambar gagal terunduh
        from moviepy.editor import ColorClip
        bg = ColorClip(size=(1080, 1920), color=(20, 20, 30), duration=duration)

    # Render video
    video = CompositeVideoClip([bg]).set_audio(audio)
    video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"✅ Video berhasil dibuat: {output_path} (Durasi: {duration:.1f} detik)")

if __name__ == "__main__":
    build_video()
