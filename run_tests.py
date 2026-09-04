import os
import sys

# اضافه کردن مسیر src به sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

test_files = [
    "tests/test_core_config.py",
    "tests/test_chat_status.py",
    "tests/test_base_strategy.py",
    "tests/test_openai_strategy.py",
    "tests/test_event_dispatcher.py",
]

print("🧪 Running all tests...\n")
print("=" * 60)

for test in test_files:
    print(f"\n=== Running {test} ===")
    result = os.system(f"python {test}")
    if result != 0:
        print(f"❌ {test} FAILED!")
    else:
        print(f"✅ {test} PASSED!")

print("\n" + "=" * 60)
print("\n✅ All tests completed!")