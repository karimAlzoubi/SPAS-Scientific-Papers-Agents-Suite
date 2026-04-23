import os
import shutil
from pathlib import Path
from podcast_pipeline import generate_audio  # هذا هو ملف app.py بعد تعديل اسمه

def main():
    # 1. إعداد المسارات
    input_pdf = "paper.pdf" # ضع مسار الورقة العلمية هنا
    output_dir = Path("./podcast_output").resolve()
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🎙️ Starting SPAS Podcast Agent for: {input_pdf}")
    
    # 2. تشغيل العقل المدبر لتوليد البودكاست
    # يتم قراءة الورقة، توليد الحوار، وتحويله إلى صوت
    audio_path, transcript = generate_audio(
        files=[input_pdf],
        url=None,
        question=None,
        tone="professional", # يمكنك تغييره إلى casual أو humorous
        length="medium",     # طول البودكاست: short, medium, long
        language="English",  # لغة البودكاست
        use_advanced_audio=False
    )
    
    # 3. نقل الملفات الصوتية والنصية إلى مجلد المخرجات
    if audio_path and os.path.exists(audio_path):
        final_audio = os.path.join(output_dir, "academic_podcast.mp3")
        shutil.move(audio_path, final_audio)
        print(f"✅ Podcast Audio saved to: {final_audio}")
        
    if transcript:
        with open(os.path.join(output_dir, "transcript.txt"), "w", encoding="utf-8") as f:
            f.write(transcript)
        print("✅ Dialogue Transcript saved.")

if __name__ == "__main__":
    main()