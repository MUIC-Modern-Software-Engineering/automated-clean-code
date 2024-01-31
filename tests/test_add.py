"""Module docstring describing the purpose of the module."""

import unittest

from . import fibonacci, is_palindrome


class TestLeetCode(unittest.TestCase):
    """TestLeetCode class for testing leetcode module."""

    def test_is_palindrome(self: "TestLeetCode") -> None:
        """Test is_palindrome function."""
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("hello world"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))

    def test_fibonacci(self: "TestLeetCode") -> None:
        """Test fibonacci function."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)


if __name__ == "__main__":
    unittest.main()
