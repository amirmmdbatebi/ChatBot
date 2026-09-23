import os
from dotenv import load_dotenv
load_dotenv()
"""Application configuration."""

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://apihub.agnes-ai.com/v1"
MODEL = "agnes-2.5-flash"

SYSTEM_PROMPT = (
    "You are a professional insurance sales assistant. "
    "Help users choose suitable insurance plans. Reply in the user's language."
)