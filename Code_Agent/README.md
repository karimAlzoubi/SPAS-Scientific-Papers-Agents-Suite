# 💻 Autonomous Code Generation Agent

## Overview
The **Code Agent** is an advanced, autonomous AI pipeline designed to bridge the gap between theoretical scientific research and practical software implementation. It takes a scientific paper (provided in structured JSON or LaTeX format) and automatically generates a complete, modular, and executable code repository that reproduces the methodology, model architecture, and experiments described in the paper.

Instead of relying on simple prompt-to-code generation, this agent employs a highly structured **Multi-Stage Agentic Workflow**. It thinks like a software engineer: starting with high-level architectural planning, moving to deep logical analysis of equations and algorithms, and finally executing the code generation file by file.

---

## 🧠 Agent Pipeline & Architecture

The system operates through a sequential, multi-agent pipeline to ensure the generated codebase is faithful to the paper, scalable, and mathematically sound:

### Stage 1: Document Parsing & Preprocessing
Before any code is written, the agent processes the input paper to extract clean text, removing unnecessary formatting, references, and citations. This ensures the LLM focuses purely on the methodology and experimental setup.

### Stage 2: Strategic Planning & Architecture (`Planning Agent`)
Acts as the **System Architect**. 
- It reads the entire paper and drafts a comprehensive roadmap for reproducing the method.
- It designs the software architecture, determining which files are needed (e.g., `model.py`, `dataset.py`, `train.py`).
- It extracts core hyperparameters and builds a foundational `config.yaml` to govern the entire project.

### Stage 3: Deep Logic Analysis (`Analysis Agent`)
Acts as the **Research Scientist**.
- It takes the high-level plan and conducts a deep dive into the mathematical equations, algorithms, and data processing steps.
- It maps the theoretical concepts to specific functions and classes defined in the architectural plan, ensuring no mathematical detail is lost in translation.

### Stage 4: Code Generation (`Coding Agent`)
Acts as the **Senior Software Engineer**.
- Using the configurations, architectural plan, and detailed logic analysis, this agent writes the actual Python code.
- It generates the codebase file by file in an iterative manner, strictly adhering to best practices (e.g., strong typing, modularity, and avoiding circular imports).
- It ensures all variables and hyperparameters are dynamically loaded from the generated `config.yaml`.

### Stage 5: Self-Correction (`Debugging Agent`)
Acts as the **QA Tester**.
- If the generated code encounters runtime errors, this module analyzes the execution logs.
- It proposes precise `SEARCH / REPLACE` patches to fix logical bugs, syntax errors, or missing dependencies without rewriting the entire file.

---

## 🌟 Key Features

- **Multi-Model Support:** Built to work seamlessly with cutting-edge proprietary models (via OpenAI API) and large open-source models (via vLLM).
- **Format Agnostic:** Capable of processing both JSON-parsed PDFs and raw LaTeX source files.
- **Dependency Aware:** Automatically detects necessary libraries (e.g., PyTorch, NumPy) and Hugging Face model IDs required to run the final repository.
- **Modular Output:** Does not output a single messy script. Instead, it builds a properly structured repository directory ready for execution.