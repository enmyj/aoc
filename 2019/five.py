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

        print(pnt, ls)

        ipnt = str(ls[pnt])
        op_cd = ipnt.zfill(5)[-2:]
        instr = ipnt.zfill(5)[0:-2][::-1]
        
        if op_cd == '99':
            return ls
        elif op_cd == '01':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]
            ls[ls[pnt+3]] = param1+param2
            pnt += 4
        elif op_cd == '02':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]
            ls[ls[pnt+3]] = param1*param2
            pnt += 4
        elif op_cd == '03':
            ls[ls[pnt+1]] = inp
            pnt += 2
        elif op_cd == '04':
            print(pnt, ls)
            break
            print(ls[ls[pnt+1]])
            pnt += 2
        elif op_cd == '05':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]
            if param1 != 0:
                ls[pnt] = ls[param2]
            else:
                pnt += 3
        elif op_cd == '06':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]

            if param1 == 0:
                ls[pnt] = ls[param2]
            else:
                pnt += 3

        elif op_cd == '07':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]
            if param1 < param2:
                ls[ls[pnt+3]] = 1
            else:
                ls[ls[pnt+3]] = 0
            pnt += 4
        elif op_cd == '08':
            param1 = ls[ls[pnt+1]] if instr[0] == '0' else ls[pnt+1]
            param2 = ls[ls[pnt+2]] if instr[1] == '0' else ls[pnt+2]
            if param1 == param2:
                ls[ls[pnt+3]] = 1
            else: 
                ls[ls[pnt+3]] = 0
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

    print(intcode(
        [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
        0
    ))

    # answers
    # fp = '/home/imyjer/repos/aoc/2019/data/five.input'
    # print(q5a(read_input(fp)))
    # print(q6a(fp))
