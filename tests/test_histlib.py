from automated_clean_code.exercise_20_histlib import fill_up_histogram, find_max_and_min_key


def test_find_max_key():
    res = find_max_and_min_key({"k": 13, "n": 123, "l": 3})
    max_count_right = res.max_counter == 123
    max_key_right = res.max_key == "n"
    min_count_right = res.min_counter == 3
    min_key_right = res.min_key == "l"
    assert max_count_right and max_key_right and min_count_right and min_key_right


def test_fill_up_histogram(simple_test_data_file: str):
    res = fill_up_histogram(simple_test_data_file)
    got_a = 3 == res.get("a")
    got_b = 2 == res.get("b")
    got_c = 3 == res.get("c")
    assert got_b and got_a and got_c
