# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from typing import Dict, List, Optional


def get_file_name_from_args(args: List[str]) -> str:  # pragma: no cover
    """Retrieve file name from arguments passed in."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args()
    return args.filename


class MinMax:
    """Return result."""

    max_counter: int = 0
    max_key: Optional[str] = None
    min_counter: int = 0
    min_key: Optional[str] = None


def fill_up_histogram(filename: str) -> Dict[str, int]:
    """Fill up the histogram.

    Args:a
      filename (string): The name of the file being read from
    Returns:
      (int). The sum of the two numbers.
    """
    counter = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 1
    return counter


def main():  # pragma: no cover
    """Initiate the main entry point."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args()

    counter = fill_up_histogram(args.fname)

    # find max and min key
    max_counter, max_key, min_counter, min_key = find_max_and_min_key(counter)

    print(f"Min Key = {min_key} with count = {min_counter}")
    print(f"Max Key = {max_key} with count = {max_counter}")


def find_max_and_min_key(counter: Dict[str, int]) -> MinMax:
    """Find the max and min key given a histogram.

    Returns:
      Tuple[int, str, int, str]. max_counter, max_key, min_counter, min_key
    """
    ret = MinMax()
    for line, count in counter.items():
        if ret.max_key is None or count > ret.max_counter:
            ret.max_key = line
            ret.max_counter = count
        if ret.min_key is None or count < ret.min_counter:
            ret.min_key = line
            ret.min_counter = count
    return ret


if __name__ == "__main__":
    main()
