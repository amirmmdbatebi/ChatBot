from .base_observer import ChatObserver
from core.chat_status import ChatStatus

class StatusDisplayObserver(ChatObserver):
    def __init__(self):
        self._current_status = ChatStatus.IDLE
    
    def on_message_received(self, user_message: str, bot_response: str) -> None:
        pass
    
    def on_error(self, error_message: str) -> None:
        print(f"\n⚠️ وضعیت: خطا - {error_message}")
    
    def on_status_change(self, status: ChatStatus) -> None:
        self._current_status = status
        icon = status.get_icon()
        description = status.get_description()
        print(f"\n{icon} وضعیت: {description}")
    
    def get_current_status(self) -> ChatStatus:
        return self._current_status 