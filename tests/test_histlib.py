from automated_clean_code.exercise_20_histlib import create_histrogram


def test_histrogram():
    example_list = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7]
    got = create_histrogram(example_list)
    result = {1: 2, 2: 3, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
    assert got == result

    example_list = [1, 1, 1, 1, 1]
    got = create_histrogram(example_list)
    result = {1: 5}
    assert got == result


def test_histrogram_with_zero_list():
    example_list = []
    got = create_histrogram(example_list)
    result = {}
    assert got == result
