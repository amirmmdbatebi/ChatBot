import sys
import os

# اضافه کردن مسیر src به sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.event_dispatcher import EventDispatcher
from core.chat_status import ChatStatus


class MockObserver:
    def __init__(self):
        self.called = False
        self.last_user_message = None
        self.last_bot_response = None
    
    def on_message_received(self, user_message: str, bot_response: str) -> None:
        self.called = True
        self.last_user_message = user_message
        self.last_bot_response = bot_response
    
    def on_error(self, error_message: str) -> None:
        pass
    
    def on_status_change(self, status: ChatStatus) -> None:
        pass


def test_event_dispatcher():
    dispatcher = EventDispatcher()
    observer = MockObserver()
    
    dispatcher.attach(observer)
    dispatcher.notify_message("سلام", "سلام! چطور میتونم کمک کنم؟")
    
    assert observer.called == True
    assert observer.last_user_message == "سلام"
    assert observer.last_bot_response == "سلام! چطور میتونم کمک کنم؟"
    print("✅ Test event dispatcher passed!")


def test_attach_detach():
    dispatcher = EventDispatcher()
    observer1 = MockObserver()
    observer2 = MockObserver()
    
    dispatcher.attach(observer1)
    dispatcher.attach(observer2)
    assert dispatcher.get_observer_count() == 2
    
    dispatcher.detach(observer1)
    assert dispatcher.get_observer_count() == 1
    print("✅ Test attach/detach passed!")


if __name__ == "__main__":
    test_event_dispatcher()
    test_attach_detach()
    print("\n🎉 All event dispatcher tests passed!")