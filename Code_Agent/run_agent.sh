#!/bin/bash

# ==========================================
# SPAS: Code Agent Execution Pipeline
# ==========================================

# إعدادات التشغيل (يمكنك تغييرها لاحقاً حسب ورقتك)
GPT_VERSION="o3-mini"
PAPER_NAME="SamplePaper"
INPUT_DIR="./inputs"
OUTPUT_DIR="./outputs/${PAPER_NAME}"
OUTPUT_REPO_DIR="./outputs/${PAPER_NAME}_repo"

PDF_JSON_PATH="${INPUT_DIR}/${PAPER_NAME}.json"
PDF_JSON_CLEANED_PATH="${INPUT_DIR}/${PAPER_NAME}_cleaned.json"

mkdir -p $INPUT_DIR
mkdir -p $OUTPUT_DIR
mkdir -p $OUTPUT_REPO_DIR

echo "🚀 Starting Agent Pipeline for: $PAPER_NAME"

echo "➡️ Stage 1: Preprocessing PDF..."
python 0_pdf_process.py \
    --input_json_path ${PDF_JSON_PATH} \
    --output_json_path ${PDF_JSON_CLEANED_PATH}

echo "➡️ Stage 2: Planning & Architecture..."
python 1_planning.py \
    --paper_name $PAPER_NAME \
    --gpt_version ${GPT_VERSION} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR}

python 1.1_extract_config.py \
    --paper_name $PAPER_NAME \
    --output_dir ${OUTPUT_DIR}

cp -rp ${OUTPUT_DIR}/planning_config.yaml ${OUTPUT_REPO_DIR}/config.yaml

echo "➡️ Stage 3: Logic Analysis..."
python 2_analyzing.py \
    --paper_name $PAPER_NAME \
    --gpt_version ${GPT_VERSION} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR}

echo "➡️ Stage 4: Code Generation..."
python 3_coding.py  \
    --paper_name $PAPER_NAME \
    --gpt_version ${GPT_VERSION} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR} \
    --output_repo_dir ${OUTPUT_REPO_DIR}

echo "✅ Pipeline Finished Successfully. Code is ready in: $OUTPUT_REPO_DIR"