import histlib


def test_make_histogram():
    test_text = "hello" "hello"
    histogram = histlib.make_histogram(test_text)
    assert histogram == {"h": 2, "e": 2, "l": 4, "o": 2}


def test_make_histogram_2():
    test_text = "heello"
    histogram = histlib.make_histogram(test_text)
    assert histogram == {"h": 1, "e": 2, "l": 2, "o": 1}
