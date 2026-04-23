# 🎙️ Autonomous Podcast Generation Agent

## Overview
The **Podcast Agent** is an innovative audio-synthesis module within the **Scientific Papers Agents Suite (SPAS)**. It autonomously reads dense scientific papers and transforms them into engaging, conversational audio podcasts. 

Instead of generating a monotonous robotic summary, this agent employs a **multi-host dialogue framework**. It uses advanced Large Language Models (LLMs) to extract key findings, methodologies, and limitations from the paper, formats them into a natural back-and-forth conversation, and synthesizes the final output using high-quality Text-to-Speech (TTS) models.

---

## 🧠 Agentic Workflow & Architecture

The pipeline operates completely headlessly (without UI interventions) and consists of three seamlessly integrated sub-agents:

### 1. Document Ingestion & Parsing (`Parser Agent`)
The agent accepts academic PDFs (or direct URLs) and extracts the raw textual content. It filters out noise and prepares a clean, continuous text stream that fits within the LLM's context window.

### 2. Scriptwriting (`Dialogue Agent`)
Acting as a professional podcast producer, this agent takes the raw academic text and writes a dynamic script.
- **Structured Output:** It forces the LLM to output a strictly formatted JSON schema representing a dialogue array.
- **Role Assignment:** It creates a natural interplay between a Host (asking guiding questions) and a Guest/Expert (explaining technical details).
- **Adaptability:** The script dynamically adapts to the user's preferred tone (e.g., Professional, Fun) and length (Short, Medium).

### 3. Audio Synthesis (`TTS Agent`)
The generated script is fed line-by-line into an advanced TTS engine.
- **Voice Mapping:** Assigns distinct, natural-sounding voices to the Host and the Guest.
- **Audio Stitching:** Synthesizes each dialogue line individually, then seamlessly concatenates them into a single, broadcast-ready audio file.

---

## 🌟 Key Features
- **Conversational Format:** Breaks down complex academic jargon into easily digestible, engaging dialogue that feels like a real radio show.
- **Multi-Language Support:** Capable of generating podcasts in multiple languages depending on the selected TTS backend.
- **Transcript Generation:** Automatically outputs a complete text transcript (`.txt`) alongside the audio file (`.mp3`) for accessibility and quick review.
- **Headless Execution:** Designed to run autonomously as a backend script, perfect for batch processing multiple papers overnight.

---

## 🛠️ Setup & Execution

### 1. Prerequisites
Ensure you have the required audio processing libraries (like `ffmpeg`) installed on your system. Then, install the Python dependencies:
```bash
pip install -r requirements.txt
```

### 2. API Configuration
By default, this agent uses **Fireworks AI** for script generation to ensure lightning-fast structured outputs. Ensure you export your API key before running:
```bash
export FIREWORKS_API_KEY="your-api-key-here"
```
*(Note: If you prefer using OpenAI, Anthropic, or local models, you can easily swap the client initialization inside `utils.py`).*

### 3. Quick Start
To generate an audio podcast from a research paper, modify the target PDF path in the run script and execute:
```bash
python run_agent.py
```

---

## 📂 Output Structure

Upon successful execution, the agent will create a dedicated output folder containing:
```text
podcast_output/
├── academic_podcast.mp3    # 🎧 The final stitched audio podcast
└── transcript.txt          # 📜 The full dialogue script
```
```