import pandas as pd


class Histogram:
    """

    Enum-like class to represent a histogram of characters in a text file.

    Attributes:
        character (str): the character to represent
        count (int): the count of the character
    """

    character: str
    count: int


class MaxMin:
    """

    Enum-like class to represent the max and min characters in a text file.

    Attributes:
        max (Histogram): the max character
        min (Histogram): the min character
    """

    max: Histogram
    min: Histogram


def load_text_file(fname: str) -> str:
    """
    Load a text file and returns the contents as a string.

    Args:
        fname (str): the file name
    Returns:
        (str). The contents of the file.
    """
    with open(fname, "r") as f:
        return f.read()


def find_max_char_occurence(text: str) -> Histogram:
    """
    Find the max occurences of a character in a string.

    Args:
        text (str): the text to search
    Returns:
        (Histogram). The max character and count.
    """
    h = Histogram()
    h.character = pd.Series(list(text)).value_counts().idxmax()
    h.count = pd.Series(list(text)).value_counts().max()
    return h


def find_min_char_occurence(text: str) -> Histogram:
    """
    Find the min occurences of a character in a string.

    Args:
        text (str): the text to search
    Returns:
        (Histogram). The min character and count.
    """
    h = Histogram()
    h.character = pd.Series(list(text)).value_counts().idxmin()
    h.count = pd.Series(list(text)).value_counts().min()
    return h


def find_min_max_char_occurnces_in_file(fname: str) -> MaxMin:
    """
    Search a file for the max and min characters.

    Args:
        fname (str): the file name
    Returns:
        (MaxMin). The max and min characters and counts.
    """
    text = load_text_file(fname)
    max_char = find_max_char_occurence(text)
    min_char = find_min_char_occurence(text)
    maxmin = MaxMin()
    maxmin.max = max_char
    maxmin.min = min_char
    return maxmin
