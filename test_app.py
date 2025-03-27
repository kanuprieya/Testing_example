"""Unit tests for app.py."""  # Module docstring

import unittest
import app

class TestApp(unittest.TestCase):
    """Test cases for app module."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(app.add(2, 3), 5)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(app.subtract(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
