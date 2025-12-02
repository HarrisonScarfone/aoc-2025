FILEPATH = "C:\\Users\\harry\\Desktop\\aoc2025\\day2\\input.txt"

def get_input(fp=FILEPATH):
    with open(fp, "r") as f:
        return [elem.strip() for elem in f.readlines()]

def part1():
    arr = get_input()[0]
    result = 0

    for elem in arr.split(","):
        id1, id2 = elem.split("-")
        low, high = int(id1), int(id2)

        for i in range(low, high+1):
            n = str(i)
            ls = n[:len(n)//2]
            rs = n[len(n)//2:]
            if ls == rs:
                result += i

    return result

def validate_id(val):
    n = len(val)

    for size in range(1, n):
        if n % size != 0:
            continue

        pattern = val[:size]
        if pattern * (n // size) == val:
            return int(val)

    return 0

def part2():
    arr = get_input()[0]
    result = 0

    for elem in arr.split(","):
        id1, id2 = elem.split("-")

        low, high = int(id1), int(id2)

        for i in range(low, high+1):
            result += validate_id(str(i))

    return result

print("Part 1: ", part1())
print("Part 1: ", part2())
