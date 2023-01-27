import argparse
import sys
from typing import Dict, List

from .histogram_statistics import HistogramStatistics, KeyValuePair


def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def fill_histogram_from_list(list_of_strings: List[str]) -> Dict[str, int]:
    """Convert a list of string into a histogram.

    Args:
        list_of_strings: list of strings

    Returns:
        a histogram (dictionary of the frequency of each string)
    """
    counter: Dict[str, int] = {}
    for line in list_of_strings:
        line = line.strip()
        counter[line] = counter.get(line, 0) + 1
    return counter


def fill_histogram_from_file(fname: str) -> Dict[str, int]:
    """Convert a file into a histogram.

    Args:
        fname: a string (name of the file)

    Returns:
        a histogram (dictionary of the frequency of each string)
    """
    with open(fname, "r") as f:
        return fill_histogram_from_list(f)


def compute_histogram_statistics(histogram: Dict[str, int]) -> HistogramStatistics:
    """Compute min and max frequency values of a histogram.

    Args:
        histogram: a dictionary

    Returns:
        statistics (min and max key-value pairs)
    """
    max_key_value_pair: KeyValuePair = KeyValuePair("", 0)
    min_key_value_pair: KeyValuePair = KeyValuePair("", sys.maxsize)

    for k, v in histogram.items():
        if max_key_value_pair is None or v > max_key_value_pair.value:
            max_key_value_pair = KeyValuePair(k, v)
        if min_key_value_pair is None or v < min_key_value_pair.value:
            min_key_value_pair = KeyValuePair(k, v)

    return HistogramStatistics(max_key_value_pair, min_key_value_pair)


def print_statistical_values_from_file(fname: str) -> None:
    """Print statistics of most and least frequent line of a given file.

    Args:
        fname: a string (name of the file)
    """
    # fill up histogram
    counter = fill_histogram_from_file(fname)

    # find max key
    statistics: HistogramStatistics = compute_histogram_statistics(counter)

    print(f"Min Key = {statistics.min_key_value_pair.key} with count = {statistics.min_key_value_pair.value}")
    print(f"Max Key = {statistics.max_key_value_pair.key} with count = {statistics.max_key_value_pair.value}")


def parse_args() -> argparse.Namespace:
    """Parse arguments using an argument parser to extract the file name."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print_statistical_values_from_file(args.fname)
