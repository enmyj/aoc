import re

from utils import read_file_into_string


def part_one(filename):
    instructions = read_file_into_string(filename)
    matches: list[str] = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", instructions)

    total = 0
    for left, right in matches:
        total += int(left) * int(right)

    return total


def part_two(filename):
    instructions = read_file_into_string(filename)
    matches: list[str] = re.findall(
        r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", instructions
    )

    multiply = True
    total = 0
    for left, right, do, dont in matches:
        if dont:
            multiply = False
            continue
        if do:
            multiply = True
            continue

        if multiply:
            total += int(left) * int(right)

    return total


if __name__ == "__main__":
    filename = "three.txt"
    print(part_one(filename))
    print(part_two(filename))
