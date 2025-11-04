from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not OPENAI_API_KEY:
    print("⚠️ Warning: OPENAI_API_KEY not set in .env")
