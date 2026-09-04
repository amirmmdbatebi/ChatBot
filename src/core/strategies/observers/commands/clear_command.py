from typing import Optional
from .base_command import Command
from core.chat_bot import ChatBot


class ClearCommand(Command):
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        confirm = input("آیا از پاک کردن تاریخچه مطمئن هستید؟ (y/n): ").strip().lower()
        if confirm in ['y', 'yes', 'بله']:
            chat_bot.clear_history()
            print("\n🗑️ تاریخچه مکالمه پاک شد")
        else:
            print("\n❌ عملیات لغو شد")
        
        return True
    
    def get_name(self) -> str:
        return "clear"
    
    def get_help(self) -> str:
        return "پاک کردن تاریخچه مکالمه"
    
    def get_aliases(self) -> list:
        return ["پاک"]