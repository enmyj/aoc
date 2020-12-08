from pathlib import Path
import re
from typing import Dict

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

    return valid


def question_two(puzzle_input: Dict) -> int:
    """ Looks boring! Was boring!
    """
    valid_passports = []
    invalid_passports = []
    for key, value in puzzle_input.items():
        if not check_integers(value.get("byr", False), 1920, 2002):
            invalid_passports.append(key)
            continue
        if not check_integers(value.get("iyr", False), 2010, 2020):
            invalid_passports.append(key)
            continue
        if not check_integers(value.get("eyr", False), 2020, 2030):
            invalid_passports.append(key)
            continue
        if not check_hgt(value.get("hgt", False)):
            invalid_passports.append(key)
            continue
        if not check_hcl(value.get("hcl", False)):
            invalid_passports.append(key)
            continue
        if not check_ecl(value.get("ecl", False)):
            invalid_passports.append(key)
            continue
        if not check_pid(value.get("pid", False)):
            invalid_passports.append(key)
            continue

        valid_passports.append(key)

    return len(valid_passports)


def check_integers(val, min_: int, max_: int) -> bool:
    if val is False:
        return False

    try:
        val = int(val)
        return min_ <= val <= max_
    except Exception:
        return False


def check_hgt(val) -> bool:
    if val is False:
        return False

    if "cm" in val:
        return 150 <= int(val.strip("cm")) <= 193
    elif "in" in val:
        return 59 <= int(val.strip("in")) <= 76
    else:
        return False


def check_hcl(val) -> bool:
    if val is False:
        return False

    return bool(re.match(r"^#([0-9]|[a-z]){6}$", val))


def check_ecl(val) -> bool:
    return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(val) -> bool:
    if val is False:
        return False

    return bool(re.match(r"^[0-9]{9}$", val))


if __name__ == "__main__":
    puzzle_input = read_input()
    print(question_one(puzzle_input))
    print(question_two(puzzle_input))
