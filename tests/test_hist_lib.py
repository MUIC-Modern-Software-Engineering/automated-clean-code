from automated_clean_code import hist_lib as hl


def test_make_histogram():
    got = hl.make_histogram(["a", "b", "a"])
    assert got == {"a": 2, "b": 1}


def test_min_max_key_str():
    stat = hl.MinMaxKey(min_key="a", min_count=10, max_key="b", max_count=30)
    assert str(stat) == "Min Key = a with count = 10\nMax Key = b with count = 30"


def test_find_min_max_key():
    counter = {"a": 2, "b": 1, "c": 3}
    stat = hl.find_min_max_key(counter)
    assert stat == hl.MinMaxKey(min_key="b", min_count=1, max_key="c", max_count=3)


def test_parse_fname_from_arg():
    argv = ["run_me", "hello.txt"]
    assert hl.parse_filename_from_argv(argv) == "hello.txt"


def test_main(simple_test_file: str, capsys: any):
    argv = ["run_me", simple_test_file]
    hl.main(argv)
    out, _ = capsys.readouterr()
    assert out == "Min Key = c with count = 1\nMax Key = d with count = 4\n"
