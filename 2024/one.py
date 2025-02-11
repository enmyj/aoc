import pathlib
from collections import Counter

data_dir = pathlib.Path(__file__).parent.resolve().joinpath("data")


def read_file():
    with open(data_dir.joinpath("one.txt")) as f:
        for line in f:
            yield line


def process_input():
    left, right = [], []
    for line in read_file():
        x, y = line.split()
        left.append(int(x))
        right.append(int(y))

    return left, right


def total_distance(left, right):
    matched = zip(sorted(left), sorted(right))
    tot = 0
    for x, y in matched:
        tot += abs(x - y)

    return tot


def similarity_score(left, right):
    count = Counter(right)
    tot = 0
    for x in left:
        tot += count[x] * x

    return tot


def day_one():
    left, right = process_input()
    print(total_distance(left, right))
    print(similarity_score(left, right))


if __name__ == "__main__":
    day_one()
