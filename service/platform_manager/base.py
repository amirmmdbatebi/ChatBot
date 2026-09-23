"""Platform Manager interface: receive, post-process and send messages."""
from abc import ABC, abstractmethod


class PlatformManager(ABC):
    @abstractmethod
    def receive_message(self) -> str | None:
        """Return user text, or None when the session should end."""

    @abstractmethod
    def post_process(self, reply: str) -> str:
        """Adapt the reply to the platform's format."""

    @abstractmethod
    def send_message(self, text: str) -> None:
        """Deliver the text to the user."""