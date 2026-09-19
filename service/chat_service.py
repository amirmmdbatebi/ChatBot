"""Service: orchestrates LLM, User State Manager and Platform Manager."""
from service.llm.fetch import LLMFetcher
from service.llm.post_process import LLMPostProcessor
from service.platform_manager.base import PlatformManager
from service.user_state.manager import UserStateManager


class ChatService:
    def __init__(
        self,
        fetcher: LLMFetcher,
        post_processor: LLMPostProcessor,
        state_manager: UserStateManager,
        platform: PlatformManager,
    ) -> None:
        self._fetcher = fetcher
        self._post_processor = post_processor
        self._state_manager = state_manager
        self._platform = platform

    def run(self, user_id: str) -> None:
        while True:
            user_text = self._platform.receive_message()
            if user_text is None:
                break
            if not user_text:
                continue
            reply = self._handle(user_id, user_text)
            self._platform.send_message(self._platform.post_process(reply))

    def _handle(self, user_id: str, user_text: str) -> str:
        self._state_manager.store(user_id, "user", user_text)
        history = self._state_manager.retrieve(user_id)
        reply = self._post_processor.process(self._fetcher.fetch(history))
        self._state_manager.store(user_id, "assistant", reply)
        return reply