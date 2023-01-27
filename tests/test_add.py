import automated_clean_code


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert automated_clean_code.add_numbers(1, 2) == 3


def test_subtract():
    assert automated_clean_code.subtract_numbers(2, -2) == 4


def nested_add_subtract():
    assert automated_clean_code.subtract_numbers(automated_clean_code.add_numbers(2, 2), 2) == 2
