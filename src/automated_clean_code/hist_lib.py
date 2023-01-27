# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


def make_histogram(lines: Iterable[str]) -> Dict[str, int]:
    """Make histogram from lines."""
    counter = {}
    for line in lines:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


@dataclass
class MinMaxKey:
    """Min and Max key + value."""

    min_key: Optional[str]
    min_count: int
    max_key: Optional[str]
    max_count: int

    def __str__(self) -> str:
        """Convert to str."""
        ret = f"Min Key = {self.min_key} with count = {self.min_count}\n"
        ret += f"Max Key = {self.max_key} with count = {self.max_count}"
        return ret


def find_min_max_key(counter: Dict[str, int]) -> MinMaxKey:
    """Find minimum and maximum key/value from the counter dictionary."""
    max_key = None
    max_count = 0
    min_key = None
    min_count = 0
    for k, v in counter.items():
        if max_key is None or v > max_count:
            max_key = k
            max_count = v
        if min_key is None or v < min_count:
            min_key = k
            min_count = v
    return MinMaxKey(min_key=min_key, min_count=min_count, max_key=max_key, max_count=max_count)


def parse_filename_from_argv(argv: List[str]) -> str:
    """Parse file name from argv."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args(argv[1:])
    return args.fname


def main(argv: List[str]):
    """Read argv parse the file name print the min and max key.

    Example Usage:
        executable aaa.txt

    """
    fname = parse_filename_from_argv(argv)
    with open(fname, "r") as f:
        counter = make_histogram(f)
    basic_stat = find_min_max_key(counter)
    print(basic_stat)


if __name__ == "__main__":
    main(sys.argv)
