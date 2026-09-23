"""Terminal implementation of the Platform Manager."""
from service.platform_manager.base import PlatformManager

EXIT_COMMANDS = {"exit", "quit", "خروج"}


class TerminalPlatform(PlatformManager):
    def receive_message(self) -> str | None:
        try:
            text = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            return None
        if text.lower() in EXIT_COMMANDS:
            return None
        return text

    def post_process(self, reply: str) -> str:
        return f"Bot: {reply}\n"

    def send_message(self, text: str) -> None:
        print(text)