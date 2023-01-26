def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def super_for_loop(n: int) -> int:
    x = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    for _ in range(n):
                        x += 1
