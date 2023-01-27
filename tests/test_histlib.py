import argparse
from os.path import dirname, join
from typing import Dict
from unittest import mock
from unittest.mock import MagicMock

import automated_clean_code.histlib as hl
from automated_clean_code.histlib import Histogram, HistogramValue


@mock.patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(fname="Test"))
def test_get_file_name_from_argv(_: MagicMock):
    assert hl.get_file_name_from_argv() == join(dirname("data"), "Test")


def test_count_occurrence_from_file():
    expected_value: Dict[str, int] = {
        "apple": 3,
        "banana": 2,
    }
    result: Dict[str, int] = hl.count_occurrence_from_file("data/exercise_20_data.txt")
    assert result == expected_value


def test_get_key_max_value():
    word_count_frequency: Dict[str, int] = {
        "apple": 3,
        "banana": 2,
    }
    expect_result: HistogramValue = HistogramValue(key="apple", value=3)
    assert hl.get_key_with_max_value(word_count_frequency) == expect_result


def test_get_key_min_value():
    word_count_frequency: Dict[str, int] = {
        "apple": 3,
        "banana": 2,
    }
    expect_result: HistogramValue = HistogramValue(key="banana", value=2)
    assert hl.get_key_with_min_value(word_count_frequency) == expect_result


def test_key_min_value_empty():
    word_count_frequency: Dict[str, int] = {}
    expect_result: HistogramValue = HistogramValue(key="", value=0)
    assert hl.get_key_with_min_value(word_count_frequency) == expect_result


def test_key_max_value_empty():
    word_count_frequency: Dict[str, int] = {}
    expect_result: HistogramValue = HistogramValue(key="", value=0)
    assert hl.get_key_with_max_value(word_count_frequency) == expect_result


@mock.patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(fname="data/exercise_20_data.txt"))
def test_get_histogram_from_file(_: MagicMock):
    expected_value: Histogram = Histogram(
        min_key=HistogramValue(key="banana", value=2), max_key=HistogramValue(key="apple", value=3)
    )
    assert hl.get_histogram_from_file() == expected_value
