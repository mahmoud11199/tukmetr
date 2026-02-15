import os
import sys
import unittest

# Ensure src/ is importable when running tests directly.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from tukmetr import add, project_status


class TestCore(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(2.5, 0.5), 3.0)

    def test_project_status(self) -> None:
        self.assertEqual(project_status(), "tukmetr-ready")


if __name__ == "__main__":
    unittest.main()
