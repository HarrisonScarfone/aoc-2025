FILEPATH = "C:\\Users\\harry\\Desktop\\aoc2025\\day3\\input.txt"

def get_input(fp=FILEPATH):
    with open(fp, "r") as f:
        return [elem.strip() for elem in f.readlines()]

def part1():
    p1_in = get_input()
    res = 0
    arr = []

    for line in p1_in:
        elem1 = max(set(list(line[:-1])))
        m_idx = line.index(elem1)
        elem2 = max(set(list(line[m_idx+1:])))
        res += int(elem1)*10 + int(elem2)

    print("Part 1 result: ", res)

def part2(SIZE=12):
    p1_in = get_input()
    elems = []
    last_idx = -1
    results = []

    for line in p1_in:
        for i in reversed(range(SIZE)):
            if len(elems) >= 12:
                break

            arr = line[last_idx+1:-i] or line[last_idx+1:]
            l = list(arr)
            s = set(l)

            if s:
                curr = max(s)
                elems.append(curr)
                last_idx += line[last_idx+1:].index(curr) + 1
            else:
                elems.append(max)
                break

            curr_length = len(line[last_idx:])
            if curr_length <= i:
                elems += list(line[last_idx:])


        results.append(int("".join(elems)))
        last_idx = -1
        elems = []

    print("Part 2 result: ", sum(results))

part1()
part2()
