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


def num_orbitals(objs: Objs) -> int:
    """
    """
    # create graph from input
    g = nx.DiGraph()
    g.add_edges_from(objs)

    # list of unique planets
    planets = list(g.nodes)
    planets.remove('COM')

    # lol there's gotta be a smarter way to do this
    cnt = 0
    for planet in planets:
        pred = list(g.predecessors(planet))[0]
        cnt += 1
        while pred != 'COM':
            pred = list(g.predecessors(pred))[0]
            cnt += 1

    return cnt


def shortest_path_to_santa(objs: Objs) -> int:
    """
    """
    # create graph from input
    g = nx.Graph()
    g.add_edges_from(objs)

    return nx.shortest_path_length(g, 'YOU', 'SAN') - 2



def q6a(objs: Objs) -> int:
    """
    """
    return num_orbitals(objs)


def q6b(objs: Objs) -> int:
    """
    """
    return shortest_path_to_santa(objs)


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
    
    assert num_orbitals(read_input(test_input, file = False)) == 42

    test_input2 = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN"""

    assert shortest_path_to_santa(read_input(test_input2, file = False)) == 4


    # answers
    fp = '/home/imyjer/repos/aoc/2019/data/six.input'
    print(q6a(read_input(fp)))
    print(q6b(read_input(fp)))
