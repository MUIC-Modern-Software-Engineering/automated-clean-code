"""Module for leetcode functions."""


def is_palindrome(s: str) -> bool:
    """Check if the input string is a palindrome."""
    s_cleaned = "".join(char.lower() for char in s if char.isalnum())
    result = s_cleaned == s_cleaned[::-1]
    print(f"""Input: {s}, Cleaned: {s_cleaned}, Result: {result}""")
    return result


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
