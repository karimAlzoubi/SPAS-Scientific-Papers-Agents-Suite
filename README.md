<div align="center">

# 🚀 SPAS: Scientific Papers Agents Suite
### From Text to Triumph: An Autonomous Multi-Agent Pipeline for Research Communication

**A Submission for the [Agenticthon](https://agenticthon.com/) Hackathon**
<br>
by **Mohammed Karim Al-Zoubi** & **Osama Shaqqi**

</div>

---

## 🎯 Our Mission
Scientific breakthroughs are often trapped within the dense, static confines of academic papers. **SPAS** is an autonomous, multi-agent ecosystem designed to transform any scientific paper into a complete suite of communication assets. With a single command, SPAS converts static text into five dynamic, ready-to-use formats: Code, Posters, Presentations, Videos, and Podcasts.

---

## ✨ Meet the Agentic Suite

### 💻 The Code Agent: *From Theory to Executable Reality*
This agent reads the methodology and mathematical logic from a paper and autonomously writes a clean, modular, and fully functional code repository to reproduce the results.

<img src="assets/code_agent_workflow.png" alt="Code Agent Workflow" width="100%">

**Internal Workflow:**
- **Planning Agent:** Designs the file structure and dependencies.
- **Analysis Agent:** Meticulously interprets equations and algorithms.
- **Coding & Debugging Agents:** Writes, tests, and autonomously debugs the Python code.

---

### 🖼️ The Poster Agent: *From Paper to Pixel-Perfect Poster*
Condenses lengthy papers into visually stunning academic posters, ready for any conference.

<img src="assets/poster_agent_teaser.jpeg" alt="Poster Agent Workflow" width="100%">

**Internal Workflow:**
- **Parser Agent:** Distills text and visual assets (figures, tables).
- **Planner Agent:** Uses a binary-tree algorithm to partition the canvas for a balanced flow.
- **Painter & Critic Loop:** Generates rendering code and uses a VLM to fix text overflows and alignment issues.

---

### 📊 The Slides Agent: *From Data to Dazzling Slides*
Transforms documents into polished presentations, ensuring every key insight is captured through its RAG-powered core.

**Click on a preview to view the full PDF presentation:**

<div align="center">

| Academic Style | Creative Style (Totoro) |
|:---:|:---:|
| [![Academic Slides](assets/academic_slides_preview.png)](assets/academic_slides.pdf) | [![Totoro Slides](assets/totoro_slides_preview.png)](assets/totoro_slides.pdf) |
| 📄 *View Academic PDF* | 📄 *View Totoro PDF* |

</div>

**Internal Workflow:**
- **RAG Engine:** Indexes the paper to prevent hallucinations and ensure no figure is missed.
- **Planning Agent:** Creates a blueprint mapping the narrative to a sequence of slides.
- **Creation Agent:** Renders final visuals with high-quality styling.

---

### 🎥 The Video Agent: *From Manuscript to Motion*
Produces dynamic video abstracts by translating academic concepts into animations and talking-head segments.

**Internal Workflow:**
- **Storyboard Agent (P-CoT):** Plans the video scene-by-scene with precise time allocation.
- **Multimodal Generator:** Autonomously executes `Manim` for math and `PyMOL` for molecular animations.
- **Self-Correction Loop:** Visually reviews frames to ensure absolute academic accuracy.

---

### 🎙️ The Podcast Agent: *From Text to Talk Show*
Converts academic jargon into a natural, two-host dialogue script and synthesizes it into a broadcast-ready podcast.

**Internal Workflow:**
- **Scriptwriting Agent:** Acts as a producer, assigning roles to a host and an expert guest.
- **Audio Synthesis Engine:** Uses multi-voice TTS for distinct, natural-sounding voices.
- **Transcript Generator:** Delivers a full text transcript alongside the `.mp3` output.

---

## 🧠 The Agentic Brain: Core Principles
1.  **Hierarchical Task Decomposition:** Complex goals are broken down into executable specialist tasks.
2.  **Autonomous Self-Correction:** "Critic" agents enable the system to debug and refine its own outputs.
3.  **Domain-Specific Expertise:** Specialization in architecture, graphic design, and video production.
4.  **Headless & Modular:** Designed for CLI execution and integration into automated workflows.

---

## 🚀 Getting Started

### 1. Clone the Suite
```bash
git clone https://github.com/YOUR-USERNAME/SPAS.git
cd SPAS
```

### 2. Quick Start Example: Generate a Poster
```bash
cd Poster_Agent
python -m new_pipeline --poster_path "paper.pdf" --model_name_t "4o" --model_name_v "4o"
```

---

## 👥 The Team
- **Mohammed Karim Al-Zoubi**
- **Osama Shaqqi**

**A submission for the Agenticthon Hackathon.**