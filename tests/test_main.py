import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import main

def test_main_exists():
    assert hasattr(main, 'main')

if __name__ == "__main__":
    test_main_exists()
    print("✅ Main exists")