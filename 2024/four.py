from utils import read_file


def part_one(filename):
    # Build grid and get horizontals
    grid = [line.strip() for line in read_file(filename)]

    # Vars
    width = len(grid[0])
    height = len(grid)
    search = []

    # Horizontals
    for h in range(height):
        search.append(grid[h])

    # Verticals
    for w in range(width):
        search.append("".join(grid[h][w] for h in range(height)))

    # Diagonals (Top-left to bottom-right)
    for d in range(-height + 1, width):
        diag = [grid[h][h - d] for h in range(max(0, d), min(height, width + d))]
        if len(diag) >= 4:
            search.append("".join(diag))

    # Diagonals (Top-right to bottom-left)
    for d in range(-height + 1, width):
        diag = [
            grid[h][width - 1 - (h - d)]
            for h in range(max(0, d), min(height, width + d))
        ]
        if len(diag) >= 4:
            search.append("".join(diag))

    return num_xmases(search)


def num_xmases(search):
    tot = 0
    for s in search:
        tot += s.count("XMAS")
        tot += s.count("SAMX")

    return tot


def part_two():
    pass


if __name__ == "__main__":
    filename = "four.txt"
    print(part_one(filename))
    # print(part_two(filename))
