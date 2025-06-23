"""Basic tests for ComfyUI-DeepSeek-Toolkit"""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

class TestBasicFunctionality(unittest.TestCase):
    def test_imports(self):
        try:
            from src.core import llm_loader
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")

if __name__ == "__main__":
    unittest.main()
