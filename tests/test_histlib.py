from automated_clean_code.exercise_20_histlib import find_freq_from_list, get_min_max_freq_from_dict


def test_freq_from_list():
    input1 = ["apple", "apple", "apple", "banana", "banana", "orange"]
    input2 = ["apple", "apple", "apple", "banana", "banana", "orange", "apple"]
    input3 = ["apple", "apple", "apple", "banana", "banana", "orange", "apple", "banana"]
    input4 = []

    output1 = {"apple": 3, "banana": 2, "orange": 1}
    output2 = {"apple": 4, "banana": 2, "orange": 1}
    output3 = {"apple": 4, "banana": 3, "orange": 1}
    output4 = {}

    assert find_freq_from_list(input1) == output1
    assert find_freq_from_list(input2) == output2
    assert find_freq_from_list(input3) == output3
    assert find_freq_from_list(input4) == output4


def test_get_min_max_from_dict():
    input1 = {"apple": 3, "banana": 2, "orange": 1}
    input2 = {"oreo": 3}

    output1 = ("apple", "orange")
    output2 = {"oreo", "oreo"}

    assert get_min_max_freq_from_dict(input1), output1
    assert get_min_max_freq_from_dict(input2), output2
