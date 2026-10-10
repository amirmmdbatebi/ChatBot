"""LLM layer - post process: cleans and normalizes the raw model output."""


class LLMPostProcessor:
    def process(self, raw_reply: str) -> str:
        return raw_reply.strip()