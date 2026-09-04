from typing import List, Dict
from openai import OpenAI
from .base_strategy import LLMStrategy
from core.exceptions import AuthenticationError, RateLimitError, StrategyError


class OpenAIStrategy(LLMStrategy):
    def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1", model: str = "gpt-3.5-turbo"):
        if not api_key:
            raise ValueError("OpenAI API key is required")
        
        self._client = OpenAI(api_key=api_key, base_url=base_url)
        self._model = model
        self._available_models = [
            "gpt-4",
            "gpt-4-turbo-preview",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k"
        ]
    
    def generate_response(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        try:
            response = self._client.chat.completions.create(
                model=self._model,
                messages=messages,
                temperature=temperature,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            raise StrategyError(f"OpenAI API Error: {str(e)}")
    
    def get_name(self) -> str:
        return "OpenAI"
    
    def get_available_models(self) -> List[str]:
        return self._available_models
    
    def get_current_model(self) -> str:
        return self._model
    
    def set_model(self, model_name: str) -> None:
        if model_name not in self._available_models:
            raise ValueError(f"مدل {model_name} در دسترس نیست")
        self._model = model_name
    
    def validate_configuration(self) -> bool:
        try:
            self._client.models.list()
            return True
        except:
            return False