from enum import Enum, auto

class ChatStatus(Enum):
    IDLE = auto()
    PROCESSING = auto()
    ERROR = auto()
    
    def get_icon(self) -> str:
        icons = {
            ChatStatus.IDLE: "💬",
            ChatStatus.PROCESSING: "⏳",
            ChatStatus.ERROR: "⚠️"
        }
        return icons.get(self, "❓")
    
    def get_description(self) -> str:
        descriptions = {
            ChatStatus.IDLE: "آماده برای دریافت پیام",
            ChatStatus.PROCESSING: "در حال پردازش...",
            ChatStatus.ERROR: "خطا رخ داده است"
        }
        return descriptions.get(self, "وضعیت نامشخص")