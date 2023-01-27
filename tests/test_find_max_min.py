from automated_clean_code.exercise_20_histlib import find_max_key


def test_max_min_key():
    example_dict = {1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 1}
    got = find_max_key(example_dict)
    result = (2, 3, 6, 1)
    assert got == result
