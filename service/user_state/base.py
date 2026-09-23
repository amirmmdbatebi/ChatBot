from abc import ABC, abstractmethod


class UserStateManager(ABC):
    @abstractmethod
    def retrieve(self, user_id: str) -> list[dict]:
        """Return the conversation history for the given user."""

    @abstractmethod
    def store(self, user_id: str, role:str, content: str) -> None:
        """Add a message with the given role and content to the user's conversation history."""
        