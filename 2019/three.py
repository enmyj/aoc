#!/usr/bin/env python3


def read_input(input_file: str) -> list:
    """ read input file into list of lists of strings
    """
    with open(input_file, 'r') as f:
        lns = f.readlines()

    return [ln.strip().split(',') for ln in lns]


def wire_to_path(wire: list) -> list:
    """ turn ordinal directions in "wire"
    into a path AKA list of (x, y) points on path
    """
    path, x, y = [], 0, 0

    for pt in wire:
        dire = pt[0]
        val = int(pt[1:])
        if dire == 'U':
            path.extend([(x, i) for i in range(y+1, y+1+val)])
            y += val
        elif dire == 'D':
            path.extend([(x, i) for i in range(y-1, y-1-val, -1)])
            y -= val
        elif dire == 'R':
            path.extend([(i, y) for i in range(x+1, x+1+val)])
            x += val
        elif dire == 'L':
            path.extend([(i, y) for i in range(x-1, x-1-val, -1)])
            x -= val

    return path


def q3a(raw_wires: str) -> int:
    """ read AOC input for all "wires"
    find intersecting points
    return manhattan distance for the closest point to (0,0)
    """
    # get points along each wire
    wires = [wire_to_path(wire) for wire in raw_wires]

    # find intersecting points between first two wires
    # (per input spec)
    intersect = list(set(wires[0]) & set(wires[1]))

    # return manhattan distance for cloest point to (0, 0)
    return min(abs(x) + abs(y) for x, y in intersect)


def q3b(input_file: str) -> int:
    """
    """
    pass


if __name__ == "__main__":

    # tests from instructions
    testwire1 = ['R8', 'U5', 'L5', 'D3']
    testwire2 = ['U7', 'R6', 'D4', 'L4']
    assert wire_to_path(testwire1) == [
        (1, 0), (2, 0), (3, 0), (4, 0),
        (5, 0), (6, 0), (7, 0), (8, 0),
        (8, 1), (8, 2), (8, 3), (8, 4),
        (8, 5), (7, 5), (6, 5), (5, 5),
        (4, 5), (3, 5), (3, 4), (3, 3),
        (3, 2)
    ]
    assert wire_to_path(testwire2) == [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (0, 5), (0, 6), (0, 7), (1, 7),
        (2, 7), (3, 7), (4, 7), (5, 7),
        (6, 7), (6, 6), (6, 5), (6, 4),
        (6, 3), (5, 3), (4, 3), (3, 3),
        (2, 3)
    ]
    assert q3a([testwire1, testwire2]) == 6

    testwire3 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    testwire4 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    assert q3a([testwire3, testwire4]) == 159

    testwire5 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    testwire6 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    assert q3a([testwire5, testwire6]) == 135

    # answers
    fp = '/Users/ian.myjer/repos/aoc/2019/data/three.input'
    print(q3a(read_input(fp)))
    print(q3b(read_input(fp)))
