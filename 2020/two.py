from pathlib import Path
from collections import Counter
from dataclasses import dataclass
from typing import List

HERE = Path(__file__).resolve().parent


@dataclass
class PasswordDetails:
    min_: int
    max_: int
    letter: str
    password: str


AllDetails = List[PasswordDetails]


def read_input() -> AllDetails:
    with open(HERE.joinpath("data/two.input")) as f:
        puzzle_input = f.readlines()

    output = []
    for ln in puzzle_input:
        policy, password = ln.split(":", 1)
        nums, letter = policy.split(" ", 1)

        min_, max_ = nums.split("-", 1)
        output.append(PasswordDetails(int(min_), int(max_), letter, password.strip()))

    return output


def question_one(puzzle_input: AllDetails) -> int:
    valid = []
    for details in puzzle_input:
        c = Counter(details.password)

        if (c[details.letter] >= details.min_) and (c[details.letter] <= details.max_):
            valid.append(details.password)

    return len(valid)


def question_two(puzzle_input: AllDetails) -> int:
    valid = []
    for details in puzzle_input:

        pos_one = details.password[details.min_ - 1] == details.letter
        pos_two = details.password[details.max_ - 1] == details.letter

        if pos_one + pos_two == 1:
            valid.append(details.password)

    return len(valid)


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question_one(puzzle_input))
    print(question_two(puzzle_input))
