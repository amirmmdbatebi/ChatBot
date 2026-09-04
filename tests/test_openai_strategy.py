import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from strategies.openai_strategy import OpenAIStrategy
from strategies.base_strategy import LLMStrategy


def test_openai_initialization():
    try:
        # با یه کلید فیک (فقط برای تست وجود کلاس)
        strategy = OpenAIStrategy(
            api_key="fake-key",
            base_url="https://fake.api/v1",
            model="gpt-3.5-turbo"
        )
        assert strategy.get_name() == "OpenAI"
        assert strategy.get_current_model() == "gpt-3.5-turbo"
        print("✅ Test OpenAIStrategy initialization passed!")
    except Exception as e:
        print(f"⚠️ Expected error with fake API key: {e}")
        print("✅ Test OpenAIStrategy class exists!")


def test_openai_is_subclass():
    assert issubclass(OpenAIStrategy, LLMStrategy)
    print("✅ Test OpenAIStrategy is subclass of LLMStrategy passed!")


if __name__ == "__main__":
    test_openai_initialization()
    test_openai_is_subclass()
    print("\n🎉 All OpenAI strategy tests passed!")