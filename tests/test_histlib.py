import argparse
from unittest import mock
from unittest.mock import MagicMock

import automated_clean_code.histlib as hl


@mock.patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(fname="Test"))
def test_get_file_name_from_argv(_: MagicMock):
    assert hl.get_file_name_from_argv() == "Test"
