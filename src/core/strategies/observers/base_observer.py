from abc import ABC, abstractmethod
from core.chat_status import ChatStatus

class ChatObserver(ABC):
    @abstractmethod
    def on_message_received(self, user_message: str, bot_response: str) -> None:
        pass
    
    @abstractmethod
    def on_error(self, error_message: str) -> None:
        pass
    
    @abstractmethod
    def on_status_change(self, status: ChatStatus) -> None:
        pass