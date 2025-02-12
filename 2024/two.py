from utils import read_file


def is_safe(line):
    l = 0
    dirs = []
    jumps = []
    for r in range(1, len(line)):
        vl = int(line[l])
        vr = int(line[r])
        dirs.append("asc" if vl - vr > 0 else "desc")
        jumps.append(abs(vl - vr))

        l += 1

    if len(set(dirs)) != 1:
        return 0

    if min(jumps) < 1 or max(jumps) > 3:
        return 0

    return 1


def part_one(filename):
    tot = 0
    for line in read_file(filename):
        line_parsed = line.split(" ")
        tot += is_safe(line_parsed)

    return tot


def part_two(filename):
    tot = 0
    for line in read_file(filename):
        line_parsed = line.split(" ")
        for i in range(len(line_parsed)):
            if (v := is_safe(line_parsed[:i] + line_parsed[i + 1 :])) == 1:
                tot += v
                break

    return tot


if __name__ == "__main__":
    filename = "two.txt"
    print(part_one(filename))
    print(part_two(filename))
