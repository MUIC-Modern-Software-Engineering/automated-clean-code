# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from dataclasses import dataclass
from os.path import dirname, join
from typing import Dict


@dataclass
class HistogramValue:
    """Dataclass to keep key and value."""

    key: str
    value: int


@dataclass
class Histogram:
    """Dataclass to keep keys with maximum value or minimum value."""

    min_key: HistogramValue
    max_key: HistogramValue


def get_file_name_from_argv() -> str:
    """Get file name from system argument.

    Returns: str (file name)
    """
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args()
    return args.fname


def count_occurrence_from_file(file_name: str) -> Dict[str, int]:
    """Count word frequency from file name.

    Args:
        file_name: str (file name)

    Returns: dictionary of word as key and frequency as value

    """
    word_counter: Dict[str, int] = {}
    file_name = join(dirname(__file__), file_name)
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().lower()
            if line in word_counter:
                word_counter[line] += 1
                continue
            word_counter[line] = 1
    return word_counter


def get_key_with_max_value(word_count_result: Dict[str, int]) -> HistogramValue:
    """Get key with maximum value from word count result.

    Args:
        word_count_result: dictionary of word as key and frequency as value

    Returns: HistogramValue (key with the highest value)

    """
    if len(word_count_result) != 0:
        max_key: str = max(word_count_result, key=word_count_result.get)
        max_value: int = word_count_result.get(max_key)
        return HistogramValue(key=max_key, value=max_value)
    return HistogramValue(key="", value=0)


def get_key_with_min_value(word_count_result: Dict[str, int]) -> HistogramValue:
    """Get key with minimum value from word count result.

    Args:
        word_count_result: dictionary of word as key and frequency as value

    Returns: HistogramValue (key with the lowest value)

    """
    if len(word_count_result) != 0:
        min_key: str = min(word_count_result, key=word_count_result.get)
        min_value: int = word_count_result.get(min_key)
        return HistogramValue(key=min_key, value=min_value)
    return HistogramValue(key="", value=0)


def get_histogram_from_file() -> Histogram:
    """Get keys with the highest value and the lowest value.

    Returns: Histogram dataclass of minimum key and maximum key

    """
    file_name: str = get_file_name_from_argv()
    word_occurrence_count_result: Dict[str, int] = count_occurrence_from_file(file_name)
    max_key: HistogramValue = get_key_with_max_value(word_count_result=word_occurrence_count_result)
    min_key: HistogramValue = get_key_with_min_value(word_count_result=word_occurrence_count_result)
    return Histogram(max_key=max_key, min_key=min_key)


if __name__ == "__main__":
    print(get_histogram_from_file())
