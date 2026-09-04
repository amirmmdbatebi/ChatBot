from typing import List
import sys
import os

# اضافه کردن مسیر src به sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from observers.base_observer import ChatObserver
from .chat_status import ChatStatus


class EventDispatcher:
    def __init__(self):
        self._observers: List[ChatObserver] = []
    
    def attach(self, observer: ChatObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: ChatObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def get_observer_count(self) -> int:
        return len(self._observers)
    
    def notify_message(self, user_message: str, bot_response: str) -> None:
        for observer in self._observers:
            try:
                observer.on_message_received(user_message, bot_response)
            except Exception as e:
                print(f"⚠️ Observer error: {e}")
    
    def notify_error(self, error_message: str) -> None:
        for observer in self._observers:
            try:
                observer.on_error(error_message)
            except Exception as e:
                print(f"⚠️ Observer error: {e}")
    
    def notify_status_change(self, status: ChatStatus) -> None:
        for observer in self._observers:
            try:
                observer.on_status_change(status)
            except Exception as e:
                print(f"⚠️ Observer error: {e}")