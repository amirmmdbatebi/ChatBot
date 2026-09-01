from openai import OpenAI
from typing import List, Dict

# ==================== Constants ====================
class Config:
    """تنظیمات پیکربندی برنامه"""
    AGNES_API_KEY = "sk-HpS4NnEuGF3lGOqaedJ6vpT3OJCt2OgpopiRHwvlBbA25kO7"
    AGNES_BASE_URL = "https://apihub.agnes-ai.com/v1"
    DEFAULT_MODEL = "agnes-2.5-flash"
    CHAT_TEMPERATURE = 0.7
    SYSTEM_PROMPT = "تو یک دستیار مفید و دوستانه هستی."


class ExitCommands:
    """دستورات خروج از برنامه"""
    EXIT_KEYWORDS = {"exit", "quit", "خروج"}


# ==================== Core Logic ====================
class AgnesChatBot:
    """
    چت‌بات مبتنی بر Agnes AI با قابلیت نگهداری تاریخچه مکالمه
    """
    
    def __init__(self, api_key: str, base_url: str, model: str):
        self.client = self._initialize_client(api_key, base_url)
        self.model = model
        self.conversation_history = self._initialize_conversation()
    
    @staticmethod
    def _initialize_client(api_key: str, base_url: str) -> OpenAI:
        """ایجاد و پیکربندی کلاینت OpenAI"""
        return OpenAI(api_key=api_key, base_url=base_url)
    
    @staticmethod
    def _initialize_conversation() -> List[Dict[str, str]]:
        """راه‌اندازی تاریخچه مکالمه با پرامپت سیستمی"""
        return [{"role": "system", "content": Config.SYSTEM_PROMPT}]
    
    def start_chat(self) -> None:
        """شروع حلقه اصلی چت"""
        self._display_welcome_message()
        
        while True:
            user_message = self._get_user_input()
            
            if self._should_exit(user_message):
                self._display_goodbye_message()
                break
            
            self._process_user_message(user_message)
    
    def _display_welcome_message(self) -> None:
        """نمایش پیام خوش‌آمدگویی"""
        print("🤖 چت‌بات Agnes آماده است!")
        print("برای خروج، بنویس: exit یا quit\n")
        print("-" * 50)
    
    @staticmethod
    def _get_user_input() -> str:
        """دریافت ورودی از کاربر"""
        return input("\n👤 شما: ").strip()
    
    @staticmethod
    def _should_exit(user_input: str) -> bool:
        """بررسی اینکه آیا کاربر درخواست خروج داده است"""
        return user_input.lower() in ExitCommands.EXIT_KEYWORDS
    
    @staticmethod
    def _display_goodbye_message() -> None:
        """نمایش پیام خداحافظی"""
        print("\n👋 خداحافظ! موفق باشی.")
    
    def _process_user_message(self, user_message: str) -> None:
        """پردازش پیام کاربر و دریافت پاسخ"""
        self._add_message_to_history("user", user_message)
        
        try:
            bot_response = self._get_bot_response()
            self._add_message_to_history("assistant", bot_response)
            self._display_response(bot_response)
        except Exception as error:
            self._rollback_last_message()
            self._handle_error(error)
    
    def _add_message_to_history(self, role: str, content: str) -> None:
        """اضافه کردن پیام به تاریخچه مکالمه"""
        self.conversation_history.append({"role": role, "content": content})
    
    def _get_bot_response(self) -> str:
        """دریافت پاسخ از مدل Agnes"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=Config.CHAT_TEMPERATURE
        )
        return response.choices[0].message.content
    
    def _rollback_last_message(self) -> None:
        """حذف آخرین پیام در صورت بروز خطا"""
        if self.conversation_history:
            self.conversation_history.pop()
    
    @staticmethod
    def _handle_error(error: Exception) -> None:
        """مدیریت و نمایش خطا"""
        print(f"\n❌ خطا: {error}")
    
    @staticmethod
    def _display_response(response: str) -> None:
        """نمایش پاسخ ربات"""
        print(f"\n🤖 ربات: {response}")


# ==================== Entry Point ====================
def main():
    """نقطه ورود اصلی برنامه"""
    chat_bot = AgnesChatBot(
        api_key=Config.AGNES_API_KEY,
        base_url=Config.AGNES_BASE_URL,
        model=Config.DEFAULT_MODEL
    )
    chat_bot.start_chat()


if __name__ == "__main__":
    main()