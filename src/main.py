import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import AppConfig
from core.chat_bot import ChatBot
from core.exceptions import ChatBotError, ConfigurationError
from strategies import StrategyFactory
from observers import ConsoleDisplayObserver, FileLoggerObserver, StatusDisplayObserver
from commands import CommandRegistry


def create_chat_bot() -> ChatBot:
    app_config = AppConfig()
    strategies = StrategyFactory.create_all_strategies()
    
    if not strategies:
        raise ConfigurationError("No LLM strategies available. Please check your configuration.")
    
    default_strategy_name = "openai" if "openai" in strategies else list(strategies.keys())[0]
    default_strategy = strategies[default_strategy_name]
    
    observers = [
        ConsoleDisplayObserver(show_timestamps=True),
        FileLoggerObserver(app_config.log_file_path),
        StatusDisplayObserver()
    ]
    
    chat_bot = ChatBot(
        strategy=default_strategy,
        config=app_config,
        observers=observers
    )
    
    chat_bot._available_strategies = strategies
    
    print(f"✅ چت‌بات با استراتژی '{default_strategy_name}' راه‌اندازی شد")
    print(f"📌 مدل: {default_strategy.get_current_model()}")
    print(f"📁 لاگ‌ها در: {app_config.log_file_path}\n")
    
    return chat_bot


def main():
    try:
        chat_bot = create_chat_bot()
        command_registry = CommandRegistry()
        
        while True:
            try:
                user_input = input("\n👤 شما: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.startswith('/'):
                    command_name = user_input[1:].strip()
                    command = command_registry.get_command(command_name)
                    
                    if command:
                        should_continue = command.execute(chat_bot)
                        if not should_continue:
                            break
                    else:
                        print(f"\n❌ دستور '{command_name}' شناخته شده نیست")
                        print("برای مشاهده راهنما از /help استفاده کنید")
                    continue
                
                response = chat_bot.send_message(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 خداحافظ!")
                break
            except ChatBotError as e:
                print(f"\n❌ خطا: {e}")
            except Exception as e:
                print(f"\n⚠️ خطای غیرمنتظره: {e}")
    
    except ConfigurationError as e:
        print(f"\n❌ خطای پیکربندی: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ خطای غیرمنتظره در راه‌اندازی: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())