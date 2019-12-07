#!/usr/bin/env python3

from typing import List

Codes = List[int]


def read_input(input_file: str) -> Codes:
    """ read input file into list format with integers
    """
    with open(input_file, 'r') as f:
        ln = f.readline()

    ln = ln.split(',')

    return [int(l) for l in ln]


def intcode(ls: list) -> list:
    """ read in list of instructions, perform designated operations
    """
    pass 



def q5a(input_file: str) -> int:
    """
    """
    pass


def q6a(input_file: str) -> int:
    """
    """
    pass


if __name__ == "__main__":

    # tests from instructions

    # answers
    fp = '/Users/ian.myjer/repos/aoc/2019/data/two.input'
    print(q5a(fp))
    print(q6a(fp))
