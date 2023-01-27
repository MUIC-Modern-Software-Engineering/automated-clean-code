from automated_clean_code.exercise_20_histlib import fill_hist_as_dict, find_max_min_key_from_dict, hist_lib


def test_fill_hist_as_dict():
    sample_input = "abc"
    sample_got = {"a": 1, "b": 1, "c": 1}

    sample_input_repeating = "aaaaaaaaa"
    got_repeating = {"a": 9}

    assert fill_hist_as_dict(sample_input) == sample_got
    assert fill_hist_as_dict(sample_input_repeating) == got_repeating


def test_fill_hist_as_dict_empty():
    sample_input = ""
    got = dict()
    assert fill_hist_as_dict(sample_input) == got


def test_find_max_min_key_from_dict():
    sample_input = {"a": 25, "b": 24, "c": 0}
    got = ("c", "a")
    assert find_max_min_key_from_dict(sample_input) == got


def test_find_max_min_key_value_from_dict_empty():
    sample_input = {}
    got = ("", "")
    assert find_max_min_key_from_dict(sample_input) == got


def test_hist_lib():
    sample_input = "/Users/karan/Desktop/numcomp/lectures/automated-clean-code/tests/sample_file"
    got = ("", "g")
    assert hist_lib(sample_input) == got


def test_hist_lib_empty():
    sample_input = "/Users/karan/Desktop/numcomp/lectures/automated-clean-code/tests/sample_file2"
    got = ("", "")
    assert hist_lib(sample_input) == got
