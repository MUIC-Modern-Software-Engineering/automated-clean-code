import argparse


def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def subtract_numbers(x: int, y: int) -> int:
    """Subtract two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The difference of the two numbers.
    """
    return x - y


def get_filename_from_args(args: list[str]) -> str:
    """Get filename from the passed arguments.

    Args:a
      args (str): arguments

    Returns:
      (str). file name
    """
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    return parser.parse_args(args).fname


def clean_line(s: str) -> str:
    """Clean the line by stripping empty spaces at both ends of the string.

    Args:a
      s (str): string

    Returns:
      (str). stripped string
    """
    return s.lower().strip()


def get_lines_from_file(filename: str) -> list:
    """Get a list of line in the file.

    Args:a
      filename (str): file name

    Returns:
      (list). list of lines in the file
    """
    lines = None
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines


def get_counter_from_list(lines: list) -> dict:
    """Get counter dictionary from list of lines.

    Args:
        lines (list): list of lines

    Returns:
        (dict). dictionary mapping from character to its occurrence
    """
    counter = {}
    for line in lines:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


def find_min_max(counter: dict) -> tuple:
    """Find min and max key and its corresponding values.

    Args:
        counter (dict): dictionary mapping from character to its occurrence

    Returns:
        (tuple). tuple in the form of (min_key, min_counter, max_key, max_counter)
    """
    min_key, max_key = [None] * 2
    min_counter, max_counter = [0] * 2
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v
    return min_key, min_counter, max_key, max_counter


def histlib(args: list[str]) -> None:  # pragma: no cover
    """Print min_key, min_counter, max_key, and max_counter of the histogram.

    Args:
        args: arguments
    """
    filename = get_filename_from_args(args)
    lines = get_lines_from_file(filename)
    counter = get_counter_from_list(lines)
    min_key, min_counter, max_key, max_counter = find_min_max(counter)
    print(f"Min Key = {min_key} with count = {min_counter}")
    print(f"Max Key = {max_key} with count = {max_counter}")
