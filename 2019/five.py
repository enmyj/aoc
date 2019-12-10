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


def intcode(ls: list, inp: int = 1) -> list:
    """ read in list of instructions, perform designated operations
    """
    pnt = 0
    while True:
        
        # halt
        if ls[pnt] == 99:
            return ls

        # opcodes 3/4
        elif ls[pnt] in (3, 4):
            if ls[pnt] == 3:
                ls[ls[pnt+1]] = inp
            else:
                print(ls[ls[pnt+1]])
            pnt += 2

        # normal 1/2 opcodes?
        if ls[pnt] == 1:
            ls[ls[pnt+3]] = ls[ls[pnt+1]] + ls[ls[pnt+2]]
            pnt += 4
        elif ls[pnt] == 2:
            ls[ls[pnt+3]] = ls[ls[pnt+1]] * ls[ls[pnt+2]]
            pnt += 4

        # longer opcodes
        else:
            instr_rev = str(ls[pnt])[0:-2].zfill(4)[::-1]
            op_cd = str(ls[pnt])[-2]

            print(ls[pnt:pnt+4], op_cd, instr_rev)

            a = ls[ls[pnt+1]] if instr_rev[0] == '0' else ls[pnt+1]
            b = ls[ls[pnt+2]] if instr_rev[1] == '0' else ls[pnt+2]
            res = a + b if op_cd == '01' else a * b
            if instr_rev[2] == '0':
                ls[ls[pnt+3]] = res
            else:
                ls[pnt+3] = res

            pnt += 4


def q5a(instr: Codes) -> int:
    """
    """
    return intcode(instr)


def q6a(input_file: str) -> int:
    """
    """
    pass


if __name__ == "__main__":

    # tests from instructions
    assert intcode([1002,4,3,4,33]) == [1002,4,3,4,99]

    # answers
    fp = '/home/imyjer/repos/aoc/2019/data/five.input'
    print(q5a(read_input(fp)))
    # print(q6a(fp))
