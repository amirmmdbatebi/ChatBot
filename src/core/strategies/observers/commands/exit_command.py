from typing import Optional
from .base_command import Command
from core.chat_bot import ChatBot


class ExitCommand(Command):
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        print("\n👋 خداحافظ! موفق باشی.")
        return False
    
    def get_name(self) -> str:
        return "exit"
    
    def get_help(self) -> str:
        return "خروج از برنامه"
    
    def get_aliases(self) -> list:
        return ["quit", "خروج"]