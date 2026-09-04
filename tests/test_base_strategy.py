import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from strategies.base_strategy import LLMStrategy


def test_base_strategy_abstract():
    # چک میکنیم که کلاس وجود داره و متدهای抽象 رو داره
    assert hasattr(LLMStrategy, 'generate_response')
    assert hasattr(LLMStrategy, 'get_name')
    assert hasattr(LLMStrategy, 'get_available_models')
    assert hasattr(LLMStrategy, 'get_current_model')
    assert hasattr(LLMStrategy, 'set_model')
    assert hasattr(LLMStrategy, 'validate_configuration')
    
    print("✅ Test LLMStrategy interface passed!")


if __name__ == "__main__":
    test_base_strategy_abstract()
    print("\n🎉 All base strategy tests passed!")