# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='compute the entry with the most occurrence and the least occurrence form a file')
    parser.add_argument('fname', metavar='N', type=str,
                        help='filename to compute the histogram')
    args = parser.parse_args()
    counter = {}
    max_key = None
    max_counter = 0
    min_key = None
    min_counter = 0

    # fill up histogram
    with open(args.fname, 'r') as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 0

    # find max key
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v

    print(f'Min Key = {min_key} with count = {min_counter}')
    print(f'Max Key = {max_key} with count = {max_counter}')


def test_writeFunction():
    with open('test_file.txt', 'w') as f:
        f.write('a\nb\nc\na\nb\n')
    f.close()
    with open('test_file.txt', 'r') as f2:
        file_1_text = f2.readlines()
        f2.close()
    with open('test_assertion.txt', 'r') as f3:
        file_2_text = f3.readlines()
        f3.close()
    assert file_1_text == file_2_text






if __name__ == '__main__':
    main()
