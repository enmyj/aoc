from utils import read_file


def is_valid_update(rules, update):
    reversed = [(r[1], r[0]) for r in rules]
    for i in range(len(update) - 1):
        if (update[i], update[i + 1]) in reversed:
            return False

    return True


def fix(rules, update):
    reversed = [(r[1], r[0]) for r in rules]

    output = []
    last = update[0]
    for val in update[1:]:
        if (last, val) in reversed:
            output.append((val, last))
        else:
            output.append((last, val))
            last = val

    return [x[0] for x in output] + [output[-1][1]]


def process_file(filename):
    rules = []
    updates = []
    for x in read_file(filename):
        if "|" in x:
            rules.append([int(y) for y in x.strip().split("|")])
        elif x == "\n":
            continue
        else:
            updates.append([int(y) for y in x.strip().split(",")])

    return rules, updates


def part_one(filename):
    rules, updates = process_file(filename)
    middles = []
    for update in updates:
        if is_valid_update(rules, update):
            print(update, update[(len(update) // 2)])
            middles.append(update[(len(update) // 2)])

    return sum(middles)


def part_two(filename):
    rules, updates = process_file(filename)
    invalids = []
    for update in updates:
        if not is_valid_update(rules, update):
            invalids.append(update)

    middles = []
    for invalid in invalids:
        while True:
            f = fix(rules, invalid)
            if is_valid_update(rules, f):
                middles.append(f[(len(f) // 2)])
                break
            else:
                invalid = f

    print(middles)
    return sum(middles)


if __name__ == "__main__":
    filename = "five.txt"
    print(part_one(filename))
    print(part_two(filename))
