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
    for i in range(0, len(ls), 4):
        if ls[i] == 1:
            ls[ls[i+3]] = ls[ls[i+1]] + ls[ls[i+2]]
        elif ls[i] == 2:
            ls[ls[i+3]] = ls[ls[i+1]] * ls[ls[i+2]]
        elif ls[i] == 99:
            return ls
        else:
            raise Exception('Invalid Optcode')


def calculate_two_a(inp: Codes) -> int:
    """ return answer for question 2 part A
    """
    instructions = read_input(inp)
    instructions[1] = 12
    instructions[2] = 2
    return intcode(instructions)[0]


def calculate_two_b(inp: Codes) -> int:
    """ return answer for question 2 part B
    can probably find a better way than double O(n^2)
    """
    for i in range(0, 100):
        for j in range(0, 100):
            instructions = read_input(inp)
            instructions[1] = i
            instructions[2] = j
            if intcode(instructions)[0] == 19690720:
                return 100 * i + j


if __name__ == "__main__":

    # tests from instructions
    assert intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == \
        [30, 1, 1, 4, 2, 5, 6, 0, 99]

    # answers
    fp = '/Users/ian.myjer/repos/aoc/2019/data/two.input'
    print(calculate_two_a(fp))
    print(calculate_two_b(fp))
