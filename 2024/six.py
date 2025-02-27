import time

from utils import read_file


def part_one(filename):
    # Build grid and get horizontals
    grid = []
    for line in read_file(filename):
        grid.append(list(line.strip()))

    # Vars
    width = len(grid[0])
    height = len(grid)

    # starting position
    for w in range(width):
        for h in range(height):
            if grid[h][w] == "^":
                x = w
                y = h

    count = 0
    _dir = grid[y][x]
    grid[y][x] = "."
    visited = []

    while y >= 0 and y <= height - 1 and x >= 0 and x <= width - 1:
        _char = grid[y][x]

        print((y, x), _dir, _char, count)

        if _char == ".":
            if (y, x) not in visited:
                visited.append((y, x))
                count += 1

            match _dir:
                case "^":
                    y -= 1
                case "<":
                    x -= 1
                case ">":
                    x += 1
                case "v":
                    y += 1

        elif _char == "#":
            match _dir:
                case "^":
                    y += 1  # back down
                    x += 1  # right
                    _dir = ">"
                case "<":
                    y -= 1  # up
                    x += 1  # back right
                    _dir = "^"
                case ">":
                    y += 1  # down
                    x -= 1  # back left
                    _dir = "v"
                case "v":
                    y -= 1  # back up
                    x -= 1  # left
                    _dir = "<"

    return count


def part_two(filename):
    pass


if __name__ == "__main__":
    filename = "six.txt"
    print(part_one(filename))
    # print(part_two(filename))
