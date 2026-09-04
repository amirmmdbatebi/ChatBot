import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class AppConfig:
    system_prompt: str = os.getenv("SYSTEM_PROMPT", "تو یک دستیار مفید و دوستانه هستی.")
    chat_temperature: float = float(os.getenv("CHAT_TEMPERATURE", "0.7"))
    max_history_length: int = int(os.getenv("MAX_HISTORY_LENGTH", "100"))
    log_file_path: str = os.getenv("LOG_FILE_PATH", "logs/chat_logs.json")

    def validate(self) -> bool:
        if not 0 <= self.chat_temperature <= 2:
            raise ValueError(f"Temperature must be between 0 and 2")
        return True


@dataclass
class OpenAIConfig:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    default_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    def validate(self) -> bool:
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is required")
        return True


@dataclass
class ClaudeConfig:
    api_key: str = os.getenv("CLAUDE_API_KEY", "")
    default_model: str = os.getenv("CLAUDE_MODEL", "claude-3-opus-20240229")

    def validate(self) -> bool:
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY is required")
        return True


@dataclass
class LocalLLMConfig:
    base_url: str = os.getenv("LOCAL_LLM_URL", "http://localhost:11434")
    default_model: str = os.getenv("LOCAL_LLM_MODEL", "llama2")

    def validate(self) -> bool:
        if not self.base_url:
            raise ValueError("LOCAL_LLM_URL is required")
        return True