import os

from automated_clean_code.exercise_20_histlib import (
    find_max_char_occurence,
    find_min_char_occurence,
    find_min_max_char_occurnces_in_file,
    load_text_file,
)


def test_load_file():
    fname = os.path.join(os.path.dirname(__file__), "./data/exercise_20_data.txt")
    example_text = """apple
banana
apple
apple
banana
"""
    text = load_text_file(fname)
    assert text == example_text


def test_find_max_char_occurence():
    text = "apple"
    h = find_max_char_occurence(text)
    assert h.character == "p"
    assert h.count == 2


def test_find_min_char_occurence():
    text = "appllee"
    h = find_min_char_occurence(text)
    assert h.character == "a"
    assert h.count == 1


def test_find_min_max_char_occurnces_in_file():
    fname = os.path.join(os.path.dirname(__file__), "./data/exercise_20_data.txt")
    maxmin = find_min_max_char_occurnces_in_file(fname)
    assert maxmin.max.character == "a"
    assert maxmin.max.count == 9
    assert maxmin.min.character == "b"
    assert maxmin.min.count == 2
