from abc import ABC, abstractmethod
from typing import Optional
from core.chat_bot import ChatBot


class Command(ABC):
    @abstractmethod
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_help(self) -> str:
        pass
    
    @abstractmethod
    def get_aliases(self) -> list:
        pass