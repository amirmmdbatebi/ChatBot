from .openai_strategy import OpenAIStrategy
from .base_strategy import LLMStrategy

class StrategyFactory:
    @staticmethod
    def create_openai_strategy(api_key: str, base_url: str = "https://api.openai.com/v1", model: str = "gpt-3.5-turbo"):
        try:
            return OpenAIStrategy(api_key=api_key, base_url=base_url, model=model)
        except Exception:
            return None
    
    @staticmethod
    def create_all_strategies():
        from core.config import OpenAIConfig
        strategies = {}
        
        openai_config = OpenAIConfig()
        try:
            openai_config.validate()
            strategies["openai"] = OpenAIStrategy(
                api_key=openai_config.api_key,
                base_url=openai_config.base_url,
                model=openai_config.default_model
            )
        except Exception:
            pass
        
        return strategies