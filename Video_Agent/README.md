# 🎥 Autonomous Video Generation Agent

## Overview
The **Video Agent** is a state-of-the-art multimodal component of the **Scientific Papers Agents Suite (SPAS)**. It completely automates the transformation of complex scientific papers into structured, highly engaging, and professional video abstracts.

Unlike traditional text-to-video tools, this agent operates on a **"Top-Down Planning, Bottom-Up Generation"** paradigm. It understands the deep semantics of an academic paper, segments it into a logical storyline, and dynamically selects the best visual medium for each scene—ranging from AI-generated b-roll and synthetic talking heads to precise mathematical animations and molecular visualizations.

---

## 🌟 Key Features
- **Hierarchical Planning:** Automatically breaks down a long document into a coherent, scene-by-scene video script.
- **Multi-Style Rendering:** Dynamically switches between different video styles (Slides, Professional/Math, Talking Heads, or General Video) based on the content of the current scene.
- **Code-Driven Animation:** Automatically writes and executes `Manim` and `PyMOL` scripts to animate complex mathematical equations and 3D protein structures.
- **Autonomous Self-Reflection:** Features a "Visual Critic" loop. If a generated scene or animation code fails to accurately represent the paper, the agent autonomously debugs and regenerates the content until quality standards are met.

---

## 🧠 Agentic Workflow & Architecture

The video generation process is orchestrated by a team of collaborative AI roles:

### 1. High-Level Planning (`Planner Agent`)
The pipeline begins by ingesting the parsed document. The Planner Agent reads the full text and designs a storyboard. It defines the logical flow of scenes, ensuring no overlapping content and a compelling narrative arc.

### 2. Low-Level Planning (P-CoT)
For each scene defined in the high-level plan, the agent assigns specific attributes:
- **Style:** (e.g., Talking Head, Mathematical Animation).
- **Audio Content:** The exact narration script for that segment.
- **Visual Prompt / Code:** The specific prompt for video generation models or the Python code required for animations.

### 3. Multimodal Generation (`Generator Agent`)
The agent routes the task to the appropriate engine:
- **TTS Engine:** Converts the script into natural-sounding voiceovers.
- **Animation Engine:** Executes generated Python code to render precise academic visualizations.
- **Video/Avatar Engine:** Synthesizes standard video clips or presenter avatars.

### 4. Review & Refinement (`Evaluator Agent`)
Before final assembly, the Evaluator acts as a quality assurance reviewer. It inspects the generated code, visuals, and prompts. If it detects hallucinations, blank frames, or logic errors, it forces the Generator to roll back, correct the mistakes, and try again.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Since this agent generates advanced video and animations, ensure your system has the following underlying dependencies installed:
- `FFmpeg` (for video processing)
- `LaTeX` (for rendering math formulas in Manim)

### 2. Python Dependencies
Navigate to the `Video_Agent` directory and install the required packages:
```bash
pip install -r requirements.txt
```

### 3. API Configuration
Open the `config.yml` file and configure your API keys for the LLMs (e.g., OpenAI, Gemini, Qwen) and any specific video/audio generation APIs you intend to use.

---

## 🚀 Quick Start

To generate a video abstract from a PDF paper, simply run the agent script:

```bash
python run_agent.py
```
*(Note: You can modify the target PDF path and desired LLM backend directly inside `run_agent.py`)*.

---

## 📂 Output Structure

Once the process is complete, the agent will generate a beautifully structured directory containing the final video and all intermediate assets:

```text
output/(PAPER_NAME)/
├── logs/
│   ├── llm_qa.md            # Complete LLM thought process and interactions
│   ├── workflow.log         # System execution logs
│   ├── highplan.txt         # The generated storyboard
│   └── final_video.mp4      # 🎬 THE FINAL CONCATENATED VIDEO ABSTRACT
├── scene_0/                 # Assets for Scene 1
│   ├── audio.wav
│   ├── video.mp4
│   └── scene0.mp4           # Merged scene
├── scene_1/                 # Assets for Scene 2
│   ├── audio.wav
│   ├── video.mp4
│   └── scene1.mp4
└── ...
```
### 4. 🎥 Video Agent (`/Video_Agent`)
**Purpose:** Automatically transforms scientific papers into professional, multimodal video abstracts.
*   **Storyboarding:** Reads the paper and plans a logical, scene-by-scene script.
*   **Dynamic Visuals:** Switches between rendering talking-heads, slide presentations, AI-generated b-roll, and coding mathematical/molecular animations (`Manim`/`PyMOL`).
*   **Self-Correction:** Visually reviews generated segments and automatically debugs rendering code to ensure academic accuracy before final video assembly.
```