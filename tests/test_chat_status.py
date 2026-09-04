import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.chat_status import ChatStatus


def test_status_enum():
    assert ChatStatus.IDLE.get_icon() == "💬"
    assert ChatStatus.PROCESSING.get_icon() == "⏳"
    assert ChatStatus.ERROR.get_icon() == "⚠️"
    
    assert ChatStatus.IDLE.get_description() == "آماده برای دریافت پیام"
    assert ChatStatus.PROCESSING.get_description() == "در حال پردازش..."
    assert ChatStatus.ERROR.get_description() == "خطا رخ داده است"
    
    print("✅ Test ChatStatus passed!")


if __name__ == "__main__":
    test_status_enum()
    print("\n🎉 All status tests passed!")