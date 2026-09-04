from typing import Optional
from .base_command import Command
from core.chat_bot import ChatBot


class ModelCommand(Command):
    def execute(self, chat_bot: ChatBot, args: Optional[str] = None) -> bool:
        current_strategy = chat_bot.get_strategy_name()
        available_models = chat_bot.get_available_models()
        current_model = chat_bot.get_current_model()
        
        print(f"\n📊 استراتژی فعلی: {current_strategy}")
        print(f"📌 مدل فعلی: {current_model}")
        
        if available_models:
            print(f"\n🔍 مدل‌های موجود:")
            for i, model in enumerate(available_models, 1):
                marker = " ✓" if model == current_model else ""
                print(f"  {i}. {model}{marker}")
            
            try:
                choice = input("\nشماره مدل مورد نظر را انتخاب کنید (یا Enter برای انصراف): ").strip()
                if choice:
                    idx = int(choice) - 1
                    if 0 <= idx < len(available_models):
                        new_model = available_models[idx]
                        chat_bot.set_model(new_model)
                        print(f"\n✅ مدل به '{new_model}' تغییر یافت")
                    else:
                        print("\n❌ شماره نامعتبر")
            except ValueError:
                print("\n❌ لطفاً یک شماره معتبر وارد کنید")
        
        return True
    
    def get_name(self) -> str:
        return "model"
    
    def get_help(self) -> str:
        return "نمایش و تغییر مدل LLM"
    
    def get_aliases(self) -> list:
        return ["مدل"]