# !/usr/bin/env python3

from typing import List
import io
import networkx as nx

Objs = List[List[str]]


def read_input(inpt: str, file: bool = True) -> Objs:
    """ read input file
    """
    if file:
        with open(inpt, 'r') as f:
            lns = f.readlines()
    else:
        with io.StringIO(inpt) as f:
            lns = f.readlines()

    return [ln.strip().split(')') for ln in lns]


def orbits(objs: Objs) -> int:
    """
    """
    # create graph from input
    g = nx.Graph()
    g.add_edges_from(objs)

    # get list of unique planets
    l, r = [], []
    for i in objs:
        l.append(i[0])
        r.append(i[1])
    all_planets = set(l + r)


    # find number of edges to left of each planet
    # ha, apparently graph can go in any direction
    ap_no_com = list(all_planets - set(['COM']))
    cnt = 0
    for planet in ap_no_com:
        left = list(g.neighbors(planet))[0]
        cnt += 1
        while left != 'COM':
            left = list(g.neighbors(left))[0]
            cnt += 1
    
    return cnt



def q6a(objs: Objs) -> int:
    """
    """
    return orbits(objs)


def q6b(input_file: str) -> int:
    """
    """
    pass


if __name__ == "__main__":

    # tests from instructions
    test_input = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L"""
    
    # assert orbits(read_input(test_input, file = False)) == 42


    # answers
    fp = '/home/imyjer/repos/aoc/2019/data/six.input'
    print(q6a(read_input(fp)))
    # print(q6b(fp))
