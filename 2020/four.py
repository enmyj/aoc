from pathlib import Path
from typing import List, Dict

HERE = Path(__file__).resolve().parent

RKEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def read_input() -> Dict:
    with open(HERE.joinpath("data/four.input")) as f:
        puzzle_input = [line.rstrip() for line in f]

    passport = ""
    outdict = {}
    counter = 0
    for row in puzzle_input:
        if row != "":
            passport += row + " "
        else:
            kvs = passport.rstrip(" ").split(" ")
            int_dict = {}
            for kv in kvs:
                key, value = kv.split(":", 1)
                int_dict[key] = value

            outdict[counter] = int_dict
            counter += 1
            passport = ""

    return outdict


def question_one(puzzle_input: Dict) -> int:
    valid = []
    for key, value in puzzle_input.items():

        diff = set(RKEYS) - set(value.keys())
        if diff == set() or diff == set(["cid"]):
            valid.append(key)

    return len(valid)


def question_two():
    """ Looks boring!
    """
    pass


def check_byr(byr):
    pass


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question_one(puzzle_input))
    # print(question_two(puzzle_input))
