from pathlib import Path
from typing import Literal

HERE = Path(__file__).resolve().parent


def read_input() -> list:
    with open(HERE.joinpath("data/five.input")) as f:
        return [line.rstrip() for line in f]


def halfzies(sequence: str, type_: Literal["row", "column"], max_: int):
    min_ = 0
    for dir_ in sequence:
        diff = max_ - min_

        # Lower Half
        if dir_ in ["F", "L"]:
            if diff == 1:
                return min_
            else:
                max_ = round((min_ + max_) // 2)

        # Upper Half
        else:
            if diff == 1:
                return max_
            else:
                min_ = round((min_ + max_) / 2)


def question_one(puzzle_input: list, ids_or_max: Literal["ids", "max"]) -> int:
    ids = []
    for seq in puzzle_input:
        row = halfzies(sequence=seq[0:7], type_="row", max_=127)
        col = halfzies(sequence=seq[7:], type_="column", max_=7)
        ids.append((row * 8) + col)

    if ids_or_max == "max":
        return max(ids)
    else:
        return ids


def question_two(puzzle_input: list) -> int:
    ids = sorted(question_one(puzzle_input, ids_or_max="ids"))
    start, end = ids[0], ids[-1]
    return set(range(start, end + 1)).difference(ids)


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question_one(puzzle_input, ids_or_max="max"))
    print(question_two(puzzle_input))
