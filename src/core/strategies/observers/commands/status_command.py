from typing import Optional
from .base_command import Command
from core.chat_bot import ChatBot


class StatusCommand(Command):
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        status = chat_bot.get_status()
        strategy = chat_bot.get_strategy_name()
        model = chat_bot.get_current_model()
        history_length = len(chat_bot.get_history())
        
        print(f"\n📊 وضعیت چت‌بات:")
        print(f"  🤖 استراتژی: {strategy}")
        print(f"  📌 مدل: {model}")
        print(f"  💬 تاریخچه: {history_length} پیام")
        print(f"  {status.get_icon()} وضعیت: {status.get_description()}")
        
        return True
    
    def get_name(self) -> str:
        return "status"
    
    def get_help(self) -> str:
        return "نمایش وضعیت فعلی"
    
    def get_aliases(self) -> list:
        return ["وضعیت"]