from pathlib import Path
from typing import List

HERE = Path(__file__).resolve().parent


def read_input() -> list:
    with open(HERE.joinpath("data/three.input")) as f:
        return [list(line.rstrip()) for line in f]


def question_one(puzzle_input: List[List], right: int = 3, down: int = 1) -> int:
    x, y = 0, 0
    len_row = len(puzzle_input[0])
    counter = 0
    while y < len(puzzle_input) - 1:
        x = (x + right) % (len_row)
        y += down
        if puzzle_input[y][x] == "#":
            counter += 1

    return counter


def question_two(puzzle_input: List[List]):
    combos = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    all_trees = 1
    for combo in combos:
        all_trees *= question_one(
            puzzle_input=puzzle_input, right=combo[0], down=combo[1]
        )

    return all_trees


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question_one(puzzle_input, 3, 1))
    print(question_two(puzzle_input))
