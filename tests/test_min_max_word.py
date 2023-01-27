import argparse
from typing import Dict, List
from unittest import mock

import pytest
from _pytest.capture import CaptureFixture

import automated_clean_code

FILE_NAME: str = "README.md"


@pytest.fixture
def filename() -> str:
    return FILE_NAME


def test_fill_histogram_from_file() -> None:
    automated_clean_code.fill_histogram_from_file("README.md")


def test_fill_histogram_from_list() -> None:
    list_of_strings: List[str] = ["apple", "apple", "cat", "dog", "cat", "apple"]
    expected_output: Dict[str, int] = {"apple": 3, "cat": 2, "dog": 1}
    assert automated_clean_code.fill_histogram_from_list(list_of_strings) == expected_output


def test_print_statistical_values_from_file(capfd: CaptureFixture[str], filename: str) -> None:
    automated_clean_code.print_statistical_values_from_file(filename)
    out, _ = capfd.readouterr()
    statistics: automated_clean_code.HistogramStatistics = automated_clean_code.compute_histogram_statistics(
        automated_clean_code.fill_histogram_from_file(filename)
    )
    printed_min: str = (
        f"Min Key = {statistics.min_key_value_pair.key} with count = {statistics.min_key_value_pair.value}"
    )
    printed_max: str = (
        f"Max Key = {statistics.max_key_value_pair.key} with count = {statistics.max_key_value_pair.value}"
    )
    assert out == f"{printed_min}\n{printed_max}\n"


@mock.patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(fname=FILE_NAME))
def test_parse_args(filename: str) -> None:
    assert automated_clean_code.parse_args() == argparse.Namespace(fname=filename)


def test_compute_histogram_statistics() -> None:
    histogram: Dict[str, int] = {
        "apple": 4,
        "pencil": 3,
        "die": 2,
    }

    statistics = automated_clean_code.HistogramStatistics = automated_clean_code.compute_histogram_statistics(histogram)
    assert statistics.max_key_value_pair.key == "apple"
    assert statistics.max_key_value_pair.value == 4
    assert statistics.min_key_value_pair.key == "die"
    assert statistics.min_key_value_pair.value == 2
