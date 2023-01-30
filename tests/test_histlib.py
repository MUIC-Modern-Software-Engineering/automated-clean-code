import automated_clean_code


def test_get_filename_from_args():
    assert automated_clean_code.get_filename_from_args(["test.txt"]) == "test.txt"


def test_clean_line():
    assert automated_clean_code.clean_line(" test ") == "test"


def test_get_lines_from_file(simple_test_data_file: str):
    assert automated_clean_code.get_lines_from_file(simple_test_data_file) == ["t", "e", "s", "t"]


def test_get_counter_from_list():
    assert automated_clean_code.get_counter_from_list(["t", "e", "s", "t"]) == {"t": 2, "e": 1, "s": 1}


def test_find_min_max():
    assert automated_clean_code.find_min_max({"t": 2, "e": 1, "s": 1}) in [("e", 1, "t", 2), ("s", 1, "t", 2)]
