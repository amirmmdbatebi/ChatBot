def build_prompt(history: list[dict], user_text: str) -> list[dict]:
    new = history.copy()
    new.append({"role": "user", "content": user_text})
    return new