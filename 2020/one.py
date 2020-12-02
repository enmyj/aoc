from pathlib import Path
from itertools import combinations

import numpy as np

HERE = Path(__file__).resolve().parent


def read_input() -> list:
    with open(HERE.joinpath("data/one.input")) as f:
        puzzle_input = f.readlines()

    return [int(x) for x in puzzle_input]


def question(puzzle_input: list, combo_size: int = 2):
    combos = combinations(puzzle_input, combo_size)
    for combo in combos:
        if sum(combo) == 2020:
            return np.prod(combo)


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question(puzzle_input, 2))
    print(question(puzzle_input, 3))
