"""Entry point: wires the layers together."""
import config
from service.chat_service import ChatService
from service.llm.fetch import LLMFetcher
from service.llm.post_process import LLMPostProcessor
from service.platform_manager.terminal import TerminalPlatform
from service.user_state.manager import InMemoryUserStateManager

TERMINAL_USER_ID = "terminal-user"


def main() -> None:
    service = ChatService(
        fetcher=LLMFetcher(config.API_KEY, config.BASE_URL, config.MODEL),
        post_processor=LLMPostProcessor(),
        state_manager=InMemoryUserStateManager(config.SYSTEM_PROMPT),
        platform=TerminalPlatform(),
    )
    service.run(TERMINAL_USER_ID)


if __name__ == "__main__":
    main()