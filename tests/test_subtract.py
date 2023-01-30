import automated_clean_code


def test_sanity():
    assert 1 - 1 == 0


def test_subtract():
    assert automated_clean_code.subtract_numbers(1, 2) == -1
