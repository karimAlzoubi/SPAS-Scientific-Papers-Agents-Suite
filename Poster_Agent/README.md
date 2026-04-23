# 🖼️ Autonomous Poster Generation Agent

## Overview
The **Poster Agent** is a sophisticated multi-agent system designed to automate the creation of professional, visually appealing academic posters directly from scientific papers. It transforms a dense, text-heavy PDF into a fully editable, well-structured PowerPoint (`.pptx`) file, mimicking the workflow of a human graphic designer.

The system employs a top-down, "visual-in-the-loop" pipeline, where content is first parsed, then strategically laid out, and finally rendered and refined through an iterative feedback cycle powered by a Vision Language Model (VLM).

---

## 🧠 Agentic Workflow & Architecture

The poster generation process is handled by a team of three specialized, collaborative agents:

### 1. Parser Agent (The Content Curator)
This agent acts as the initial content strategist. It meticulously parses the source scientific paper to distill it into a structured asset library. Its key responsibilities include:
-   **Text Extraction:** Identifying and extracting core textual sections (e.g., Title, Authors, Abstract, Methodology, Results, Conclusion).
-   **Visual Asset Extraction:** Identifying and saving all figures, charts, and tables from the paper as separate image files.
-   **Content Structuring:** Organizing the extracted text and visual assets into a clean, addressable library for the next stage.

### 2. Planner Agent (The Layout Architect)
This agent functions as the layout designer. Using the asset library created by the Parser, the Planner designs the poster's master layout.
-   **Canvas Partitioning:** It intelligently partitions the poster canvas into logical panels (e.g., for Introduction, Methods, etc.) using a **binary-tree splitting algorithm**. This ensures a logical reading flow and a visually balanced composition.
-   **Content-Panel-Mapping:** It decides *where* each section of text and each visual asset should be placed on the poster, creating a high-level blueprint for the final design.

### 3. Painter & Commenter Agents (The Iterative Design Team)
This is a powerful duo of agents working in a feedback loop to ensure the final output is polished and free of common design flaws.
-   **Painter Agent (The Coder):** This agent takes the layout blueprint and writes executable `python-pptx` code to render the content (text and images) into their designated panels on the PowerPoint slide.
-   **Commenter Agent (The Visual Critic):** After the Painter generates a version of a panel, this agent takes a snapshot of the result. It uses a **Vision Language Model (VLM)** to "see" the rendered panel and provide critical feedback, checking for issues like:
    -   Text overflowing its container.
    -   Poor alignment of elements.
    -   Awkwardly large empty spaces.

This design-and-review loop repeats, with the Painter refining the code based on the Commenter's feedback, until the panel meets the required quality standards.

---

## 🌟 Key Features

-   **Editable PowerPoint Output:** The final product is not a static image but a fully editable `.pptx` file, allowing for easy manual adjustments.
-   **Vision-in-the-Loop Correction:** Dynamically uses a VLM to visually inspect and correct design errors, a feature far more advanced than simple text-to-image generation.
-   **Automated Layout Engine:** Employs a tree-based algorithm to ensure the poster layout is both aesthetically balanced and easy to follow.
-   **Customization & Theming:** Supports style customization through configuration files, allowing control over colors, fonts, and themes.
-   **Automatic Logo Integration:** Capable of automatically detecting institution and conference names to search for and place relevant logos on the poster.