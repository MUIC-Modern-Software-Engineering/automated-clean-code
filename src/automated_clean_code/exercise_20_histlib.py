# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
from typing import Tuple


# fill up histogram
def create_histrogram(list_of_number: list) -> dict:
    """Add two numbers together.

    Args:a
     list of number(list): a list of number

    Returns:
      (Dictionary). Dictionary of key and frequency.
    """
    counter = {}
    for each_number in list_of_number:
        if each_number in counter:
            counter[each_number] += 1
        else:
            counter[each_number] = 1
    return counter

    # find max key


def find_max_key(counter: dict) -> Tuple[int, int, int, int]:
    """Add two numbers together.

    Args:a
      counter: dictionary of int and int

    Returns:
      Tuple[int,int,int,int] cool stuff.
    """
    max_key = None
    min_key = None
    max_counter = 0
    min_counter = 0

    for key, frequency in counter.items():
        if max_key is None or frequency > max_counter:
            max_key = key
            max_counter = frequency
        if min_key is None or frequency < min_counter:
            min_key = key
            min_counter = frequency

    return (max_key, max_counter, min_key, min_counter)
