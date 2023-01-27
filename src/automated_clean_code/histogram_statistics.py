from dataclasses import dataclass


@dataclass
class KeyValuePair:
    """Key-Value pair of a dictionary."""

    key: str = ""
    value: int = 0


@dataclass
class HistogramStatistics:
    """Minimum and Maximum values' Key-Value pairs."""

    max_key_value_pair: KeyValuePair = KeyValuePair("", 0)
    min_key_value_pair: KeyValuePair = KeyValuePair("", 0)
