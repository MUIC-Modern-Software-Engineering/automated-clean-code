from typing import Tuple


def main():
    """Make a histogram then print out the min key/count and max key/count.

    Args:

    Returns:
      print the output as min key, min count, max key and max count
    """
    test_text = "hello"
    histogram_dict = make_histogram(test_text)
    output: Tuple[str, int, str, int] = find_max_and_min_count(histogram_dict)
    print(f"Min Key = {output[0]} with count = {output[1]} \n Max Key = {output[2]} with count = {output[3]}")


max_key = str
max_count = int
min_key = str
min_count = int
histogram = dict[str, int]


def find_max_and_min_count(histogram_dict: dict[str, int]) -> (max_key, max_count, min_key, min_count):
    """Find max/min count and keys of the given histogram.

    Args: histogram_dict (dict[str, int): a dictionary

    Returns:
      (str) key with the max count
      (int) max count
      (str) key with the least count
      (int) min count
    """
    current_max_key = None
    current_min_key = None
    current_max_count = 0
    current_min_count = 0

    for keys, values in histogram_dict.items():
        if current_max_key is None or values > current_max_count:
            current_max_key = keys
            current_max_count = values
        if current_min_key is None or values < current_min_count:
            current_min_key = keys
            current_min_count = values
    return current_max_key, current_max_count, current_min_key, current_min_count


def make_histogram(args: str) -> histogram:
    """Make a histogram.

    Args:
        args (str) : input text


    Returns:
      dict[str, int] histogram
    """
    histogram_dict = {}

    for line in args:
        line_without_spaces = line.strip()
        for characters in line_without_spaces:
            if characters in histogram_dict:
                histogram_dict[characters] += 1
            else:
                histogram_dict[characters] = 1
    return histogram_dict


if __name__ == "__main__":
    main()
