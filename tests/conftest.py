from os.path import dirname, join

import pytest


@pytest.fixture
def simple_test_data_file() -> str:
    return join(dirname(__file__), "./fixtures/sample_file")


@pytest.fixture
def simple_empty_test_data_file() -> str:
    return join(dirname(__file__), "./fixtures/sample_file2")
