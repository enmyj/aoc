#!/usr/bin/env python3


def m2f(m: int) -> int:
    """ computer mass to fuel calc """
    return max((m // 3) - 2, 0)


def m2f_recursive(m: int) -> int:
    """
    recursively calculate the fuel required
    for each package
    """
    if m2f(m) == 0:
        return 0
    else:
        return m2f_recursive(m2f(m)) + m2f(m)


def calculate_one_a(input_file: str) -> int:
    with open(fl, 'r') as f:
        return sum(m2f(int(m)) for m in f)


def calculate_one_b(intput_file: str) -> int:
    with open(fl, 'r') as f:
        return sum(m2f_recursive(int(line)) for line in f)


if __name__ == "__main__":

    # tests
    assert m2f(14) == 2
    assert m2f(1) == 0
    assert m2f_recursive(14) == 2
    assert m2f_recursive(1969) == 966

    # answers
    fl = '/Users/ian.myjer/repos/aoc/2019/data/one.input'
    print(calculate_one_a(fl))
    print(calculate_one_b(fl))
