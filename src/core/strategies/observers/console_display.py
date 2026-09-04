from datetime import datetime
from .base_observer import ChatObserver
from core.chat_status import ChatStatus

class ConsoleDisplayObserver(ChatObserver):
    def __init__(self, show_timestamps: bool = True):
        self.show_timestamps = show_timestamps
        self._first_event = True
    
    def on_message_received(self, user_message: str, bot_response: str) -> None:
        self._ensure_welcome()
        timestamp = self._get_timestamp()
        
        print(f"\n👤 شما {timestamp}: {user_message}")
        print(f"🤖 ربات {timestamp}: {bot_response}")
        print("-" * 60)
    
    def on_error(self, error_message: str) -> None:
        timestamp = self._get_timestamp()
        print(f"\n❌ خطا {timestamp}: {error_message}")
        print("-" * 60)
    
    def on_status_change(self, status: ChatStatus) -> None:
        if status == ChatStatus.IDLE and self._first_event:
            self._show_welcome()
            self._first_event = False
        
        if status == ChatStatus.PROCESSING:
            print(f"\n⏳ در حال پردازش...", end="", flush=True)
        elif status == ChatStatus.IDLE and not self._first_event:
            print("\r", end="")
    
    def _ensure_welcome(self) -> None:
        if self._first_event:
            self._show_welcome()
            self._first_event = False
    
    def _show_welcome(self) -> None:
        welcome = [
            "\n" + "=" * 60,
            "🤖 چت‌بات هوشمند آماده است!",
            "=" * 60,
            "\n📋 دستورات ویژه:",
            "  /exit یا /quit  - خروج از برنامه",
            "  /model          - تغییر مدل LLM",
            "  /help           - نمایش راهنما",
            "  /status         - نمایش وضعیت فعلی",
            "  /clear          - پاک کردن تاریخچه مکالمه",
            "=" * 60 + "\n"
        ]
        print("\n".join(welcome))
    
    def _get_timestamp(self) -> str:
        if self.show_timestamps:
            return f"({datetime.now().strftime('%H:%M:%S')})"
        return ""