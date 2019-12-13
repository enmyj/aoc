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


def intcode(
    ls: list,
    inp: int = 1,
    diagnostic: bool = True) -> int:
    """ read in list of instructions, perform designated operations
    """
    pnt = 0
    ret = None
    while True:

        ipnt = str(ls[pnt])
        op_cd = ipnt.zfill(5)[-2:]
        instr = ipnt.zfill(5)[0:-2][::-1]

        if op_cd != '99':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]

        if op_cd not in ('03', '04', '99'):
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]

        if op_cd == '99':
            return ret
        elif op_cd == '01':
            ls[ls[pnt+3]] = param1+param2
            pnt += 4
        elif op_cd == '02':
            ls[ls[pnt+3]] = param1*param2
            pnt += 4
        elif op_cd == '03':
            ls[ls[pnt+1]] = inp
            pnt += 2
        elif op_cd == '04':
            # stupid handling for diagnostic output
            # if we need diagnostic, only return
            # output op_code before HALT
            if ls[pnt+2] == 99:
                return param1
            else:
                if diagnostic:
                    print(param1)
                else:
                    ret = param1
                pnt += 2
        elif op_cd == '05':
            if param1 != 0:
                pnt = param2
            else:
                pnt += 3
        elif op_cd == '06':
            if param1 == 0:
                pnt = param2
            else:
                pnt += 3
        elif op_cd == '07':
            ls[ls[pnt+3]] == int(param1 < param2)
            pnt += 4
        elif op_cd == '08':
            ls[ls[pnt+3]] == int(param1 == param2)
            pnt += 4


def q5a(instr: Codes) -> int:
    """
    """
    return intcode(instr)


def q5b(instr: Codes) -> int:
    """
    """
    return intcode(instr, inp=5, diagnostic=False)


if __name__ == "__main__":

    # tests from instructions
    t1_pos = [3,9,8,9,10,9,4,9,99,-1,8]
    t2_pos = [3,9,7,9,10,9,4,9,99,-1,8]
    t3_imm = [3,3,1108,-1,8,3,4,3,99]
    t4_imm = [3,3,1107,-1,8,3,4,3,99]
    t5_pos = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    t5_imm = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

    t6 = [
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
    ]

    assert intcode(t1_pos, inp=8) == 1
    assert intcode(t1_pos, inp=9) == 0
    assert intcode(t2_pos, inp=0) == 1
    assert intcode(t2_pos, inp=9) == 0

    assert intcode(t3_imm, inp=8) == 1
    assert intcode(t3_imm, inp=9) == 0
    assert intcode(t4_imm, inp=0) == 1
    assert intcode(t4_imm, inp=9) == 0

    assert intcode(t5_pos, inp=0) == 0
    assert intcode(t5_pos, inp=1) == 1
    assert intcode(t5_imm, inp=10) == 1
    assert intcode(t5_imm, inp=0) == 0

    assert intcode(t6, inp=0, diagnostic=False) == 999
    assert intcode(t6, inp=8, diagnostic=False) == 1000
    assert intcode(t6, inp=9, diagnostic=False) == 1001

    # answers
    fp = '/home/imyjer/repos/aoc/2019/data/five.input'
    print('part 1:\n')
    print(q5a(read_input(fp)))
    print('\npart 2: \n')
    print(q5b(read_input(fp)))
