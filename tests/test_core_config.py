import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.config import AppConfig


def test_app_config_defaults():
    config = AppConfig()
    assert config.chat_temperature == 0.7
    assert config.system_prompt is not None
    assert config.max_history_length == 100
    print("✅ Test AppConfig passed!")


if __name__ == "__main__":
    test_app_config_defaults()
    print("\n🎉 Config tests passed!")