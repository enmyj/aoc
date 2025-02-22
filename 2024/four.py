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


def part_two(filename):
    grid = [line.strip() for line in read_file(filename)]

    width = len(grid[0])
    height = len(grid)

    def is_xmas(x, y):
        if x + 2 > width:
            return False
        if y + 2 > height:
            return False

        top_left = grid[y][x]
        top_right = grid[y][x + 2]
        middle = grid[y + 1][x + 1]
        bottom_left = grid[y + 2][x]
        bottom_right = grid[y + 2][x + 2]
        joined = top_left + top_right + middle + bottom_left + bottom_right
        print(joined)
        return joined in ("MSAMS", "MMASS", "SSAMM", "SMASM")

    total = 0
    for y in range(height - 2):
        for x in range(width - 2):
            total += int(is_xmas(x, y))

    return total


if __name__ == "__main__":
    filename = "four.txt"
    # print(part_one(filename))
    print(part_two(filename))
