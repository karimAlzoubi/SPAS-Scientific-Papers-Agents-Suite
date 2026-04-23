# 📊 Autonomous Presentation Generation Agent

## Overview
The **Slides Agent** is a state-of-the-art, four-stage AI pipeline designed to transform long-form documents—such as research papers, reports, or articles—into professional, visually consistent presentations. It moves beyond simple text summarization by employing a sophisticated **Retrieval-Augmented Generation (RAG)** engine to ensure no critical detail, figure, or table is overlooked.

The entire workflow is managed through an intelligent checkpoint system, allowing the process to be resumed, modified, or regenerated at any stage without losing progress.

---

## 🧠 Agentic Workflow & Architecture

The system operates through a sequential, four-stage pipeline. Each stage produces a verified checkpoint, ensuring reliability and traceability from the source document to the final rendered slides.

### Stage 1: RAG Indexing (`RAG Agent`)
This is the foundational stage where the agent builds a deep, searchable knowledge base from the source documents.
-   **Universal Document Parsing:** It first parses a wide array of file formats (PDF, DOCX, etc.) into a clean, structured representation.
-   **Content Indexing:** It then indexes the entire document—including text, tables, and figures—into a powerful RAG system. This creates an intelligent, queryable index that understands the document's content and structure.
-   **Checkpoint:** `checkpoint_rag.json`

### Stage 2: Content Analysis (`Analysis Agent`)
This agent acts as a research assistant, querying the RAG index to extract and structure the document's core components.
-   **Hierarchical Extraction:** It systematically extracts the document's structure, identifying key sections, figures, and tables.
-   **Structured Mapping:** The extracted content is organized into a clean, structured map, which serves as the single source of truth for the subsequent stages.
-   **Checkpoint:** `checkpoint_summary.json`

### Stage 3: Strategic Planning (`Planning Agent`)
This agent functions as the presentation's director. Using the structured content map, it designs a high-level blueprint for the final presentation.
-   **Content Organization:** It determines the optimal flow and organization of the content, deciding which topics belong on which slides.
-   **Layout Strategy:** It generates a detailed layout plan, specifying the content, titles, and visual elements (like figures or tables) for each slide.
-   **Checkpoint:** `checkpoint_plan.json`

### Stage 4: Visual Creation (`Creation Agent`)
This is the final stage where the agent acts as a graphic designer, rendering the high-quality visual output based on the blueprint.
-   **Style Interpretation:** It takes the user's style prompt—whether a predefined theme like "academic" or a natural language description like "minimalist with a blue theme"—and translates it into visual parameters.
-   **Image Generation:** It generates the final, polished slides one by one, ensuring visual consistency across the entire presentation.
-   **Output:** A directory of high-quality images and a consolidated PDF file.

---

## 🌟 Key Features

-   **RAG-Powered Precision:** Utilizes a Retrieval-Augmented Generation (RAG) core to ensure comprehensive and accurate content extraction, eliminating the risk of overlooking critical data.
-   **Smart Checkpoint System:** Automatically saves progress at each stage, allowing for seamless resumption, style changes, or content regeneration without starting from scratch.
-   **Custom Styling Engine:** Supports both predefined professional themes and natural language descriptions for custom-tailored visual styles.
-   **Parallel Generation:** Built with an option for parallel slide generation, significantly speeding up the creation process for longer presentations.
-   **Fast Mode vs. Normal Mode:** Offers a "fast mode" that bypasses RAG indexing for quick previews and a "normal mode" for deep, comprehensive analysis of complex documents.