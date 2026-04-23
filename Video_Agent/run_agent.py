import os
from pathlib import Path
from video_agent import VideoAgent

# إعداد البيئة لتجنب مشاكل كروت الشاشة
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

def main():
    # 1. إعداد المسارات
    input_pdf = Path("sample_paper.pdf").resolve()
    output_directory = Path("output_video").resolve()
    config_file = Path("config.yml").resolve()

    print(f"🚀 Starting SPAS Video Agent for: {input_pdf.name}")

    # 2. تهيئة الوكيل الذكي
    agent = VideoAgent(
        input_path=input_pdf, 
        output_dir=output_directory, 
        llm_config_path=config_file,
        plan_by="GEMINI",        # نموذج التخطيط
        eval_by="GEMINI",        # نموذج التقييم والمراجعة
        art_work="GEMINI",       # نموذج الإبداع الفني
        with_example=True,
        with_reflection=True,    # تفعيل المراجعة الذاتية
        with_rollback=True,
        silent=False
    )

    # 3. بدء توليد الفيديو
    agent.run()
    print("✅ Video generated successfully!")

if __name__ == "__main__":
    main()