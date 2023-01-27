# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
from typing import Tuple


def fill_hist_as_dict(content: str) -> dict[str, int]:
    """Fill up histogram.

    Args:
      content (str): content in a file

    Returns:
      (dict[str, int]). dictionary of counters of string and int
    """
    key_value_counter = {}
    for line in content:
        line = line.strip()
        if line in key_value_counter:
            key_value_counter[line] += 1
        else:
            key_value_counter[line] = 1
    return key_value_counter


def find_max_min_key_from_dict(dct: dict[str, int]) -> Tuple[str, str]:
    """Find the max and min key from a dictionary.

    Args:
      dct (dict[str, int]): a number

    Returns:
      (Tuple[str, str]). tuple of min key and max key of the given dictionary
    """
    if dct == {}:
        return "", ""
    else:
        return min(dct, key=dct.get), max(dct, key=dct.get)


def hist_lib(filename: str) -> Tuple[str, str]:
    """Find the max and min key from a file given.

    Args:
      filename (str): a filename with content

    Returns:
      (Tuple[str, str]). tuple of min_key, max_key
    """
    with open(filename) as f:
        hist = fill_hist_as_dict(f.read())
        return find_max_min_key_from_dict(hist)
