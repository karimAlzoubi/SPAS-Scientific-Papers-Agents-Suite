import os
from pathlib import Path

# Key constants
CHARACTER_LIMIT = 100_000

# Cache constants
CACHE_DIR = "./podcast_cache/tmp/"
CLEAR_CACHE_OLDER_THAN = 1 * 24 * 60 * 60  # 1 day

# Error messages-related constants
ERROR_MESSAGE_NO_INPUT = "Please provide at least one PDF file or a URL."
ERROR_MESSAGE_NOT_PDF = "The provided file is not a PDF. Please upload only PDF files."
ERROR_MESSAGE_NOT_SUPPORTED_IN_MELO_TTS = "The selected language is not supported without advanced audio generation."
ERROR_MESSAGE_READING_PDF = "Error reading the PDF file"
ERROR_MESSAGE_TOO_LONG = f"The total content is too long. Please ensure the combined text is fewer than {CHARACTER_LIMIT} characters."

# LLM API-related constants (Fireworks / Llama3)
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
FIREWORKS_MAX_TOKENS = 16_384
FIREWORKS_MODEL_ID = "accounts/fireworks/models/llama-v3p3-70b-instruct"
FIREWORKS_TEMPERATURE = 0.1

# MeloTTS
MELO_API_NAME = "/synthesize"
MELO_TTS_SPACES_ID = "mrfakename/MeloTTS"
MELO_RETRY_ATTEMPTS = 3
MELO_RETRY_DELAY = 5  # in seconds

MELO_TTS_LANGUAGE_MAPPING = {
    "en": "EN", "es": "ES", "fr": "FR", "zh": "ZJ", "ja": "JP", "ko": "KR",
}

# Suno related constants
SUNO_LANGUAGE_MAPPING = {
    "English": "en", "Chinese": "zh", "French": "fr", "German": "de",
    "Hindi": "hi", "Italian": "it", "Japanese": "ja", "Korean": "ko",
    "Polish": "pl", "Portuguese": "pt", "Russian": "ru", "Spanish": "es",
    "Turkish": "tr",
}

# General audio-related constants
NOT_SUPPORTED_IN_MELO_TTS = list(set(SUNO_LANGUAGE_MAPPING.values()) - set(MELO_TTS_LANGUAGE_MAPPING.keys()))
NOT_SUPPORTED_IN_MELO_TTS =[key for key, id in SUNO_LANGUAGE_MAPPING.items() if id in NOT_SUPPORTED_IN_MELO_TTS]

# Jina Reader-related constants
JINA_READER_URL = "https://r.jina.ai/"
JINA_RETRY_ATTEMPTS = 3
JINA_RETRY_DELAY = 5