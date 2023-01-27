from os.path import dirname, join

import pytest


@pytest.fixture
def simple_test_file() -> str:
    return join(dirname(__file__), "./fixtures/test.txt")
