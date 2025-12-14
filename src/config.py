import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# choose 'openai' or 'hf' (huggingface) - auto-selects openai if key present
DEFAULT_BACKEND = "openai" if OPENAI_API_KEY else "hf"

# transformer settings (when using HF fallback)
HF_MODEL = os.environ.get("HF_MODEL", "sshleifer/distilbart-cnn-12-6")
HF_MAX_TOKENS = int(os.environ.get("HF_MAX_TOKENS", "200"))
