import automated_clean_code


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert automated_clean_code.add_numbers(1, 2) == 3


def test_multiply():
    assert automated_clean_code.test(1, 2) == 2
