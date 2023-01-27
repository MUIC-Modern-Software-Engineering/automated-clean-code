import histlib


def test_find_max_and_min_count():
    histogram_dict = {"h": 1, "e": 2, "l": 2, "o": 2}

    assert histlib.find_max_and_min_count(histogram_dict) == ("e", 2, "h", 1)


def test_find_max_and_min_count_2():
    histogram_dict = {"h": 1, "e": 2, "l": 3, "o": 2}

    assert histlib.find_max_and_min_count(histogram_dict) == ("l", 3, "h", 1)
