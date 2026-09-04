from abc import ABC, abstractmethod
from typing import List, Dict

class LLMStrategy(ABC):
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        pass
    
    @abstractmethod
    def get_current_model(self) -> str:
        pass
    
    @abstractmethod
    def set_model(self, model_name: str) -> None:
        pass
    
    @abstractmethod
    def validate_configuration(self) -> bool:
        pass