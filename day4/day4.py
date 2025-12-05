FILEPATH = "C:\\Users\\harry\\Desktop\\aoc2025\\day4\\input.txt"

def get_input(fp=FILEPATH):
    rows = None
    with open(fp, "r") as f:
        rows = [elem.strip() for elem in f.readlines()]
    
    grid = [["."] + list(row) + ["."] for row in rows]

    return [list("." * len(grid[0]))] + grid + [list("." * len(grid[0]))]

is_in_bounds = lambda grid,i,j,del_h,del_w : i + del_h >= 0 and j + del_w >= 0 and i + del_h < len(grid) and j + del_w < len(grid[0])

def check_position(grid, i, j):
    to_check = []
    for del_h in range(-1, 2):
        for del_w in range(-1,2):
            if is_in_bounds(grid,i,j,del_h,del_w):
                to_check.append((i + del_h, j + del_w))

    count = 0
    for coor_pair in to_check:
        n, m = coor_pair
        if grid[n][m] == ".":
            count += 1
    
    if count >= 5:
        return 1
    return 0


def part1():
    grid = get_input()

    result = 0

    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            if grid[i][j] == "@":
                result += check_position(grid, i, j)

    print("Part 1 result: ", result)


def part2():
    grid = get_input()
    result = 0
    cumulative_result = 0

    while True:
        for i in range(1, len(grid)):
            for j in range(1, len(grid)):
                if grid[i][j] == "@":
                    if check_position(grid, i, j):
                        result += 1
                        grid[i][j] = "."

        cumulative_result += result

        if result == 0:
            break

        result = 0

    print("Part 2 result: ", cumulative_result)


part1()
part2()
