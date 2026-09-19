"""User State Manager: stores and retrieves each user's conversation state."""


class UserStateManager:
    def __init__(self, system_prompt: str) -> None:
        self._system_prompt = system_prompt
        self._states: dict[str, list[dict]] = {}

    def retrieve(self, user_id: str) -> list[dict]:
        if user_id not in self._states:
            self._states[user_id] = [{"role": "system", "content": self._system_prompt}]
        return self._states[user_id]

    def store(self, user_id: str, role: str, content: str) -> None:
        self.retrieve(user_id).append({"role": role, "content": content})