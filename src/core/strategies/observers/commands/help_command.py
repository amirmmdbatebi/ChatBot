from typing import Optional
from .base_command import Command
from core.chat_bot import ChatBot


class HelpCommand(Command):
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        help_text = """
📋 راهنمای دستورات:

  /exit یا /quit  - خروج از برنامه
  /model          - نمایش و تغییر مدل LLM
  /help           - نمایش این راهنما
  /status         - نمایش وضعیت فعلی
  /clear          - پاک کردن تاریخچه مکالمه

💡 نکات:
  - برای چت کردن، پیام خود را تایپ کنید
  - تاریخچه مکالمه به صورت خودکار ذخیره می‌شود
"""
        print(help_text)
        return True
    
    def get_name(self) -> str:
        return "help"
    
    def get_help(self) -> str:
        return "نمایش راهنمای دستورات"
    
    def get_aliases(self) -> list:
        return ["راهنما", "?"]