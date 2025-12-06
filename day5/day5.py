FILEPATH = "C:\\Users\\harry\\Desktop\\aoc2025\\day5\\input.txt"

def get_input(fp=FILEPATH):
    blank_idx = None
    arr = []
    with open(fp, "r") as f:
        for i, elem in enumerate(f.readlines()):
            clean = elem.strip()
            if not clean:
                blank_idx = i
            arr.append(clean)
    return ([arr[:blank_idx], arr[blank_idx+1:]])


def part1():
    arr = get_input()
    ranges = []
    ids = []
    count = 0

    for elem in arr[0]:
        lo, hi = elem.split("-")
        ranges.append((int(lo), int(hi)))
    
    for elem in arr[1]:
        ids.append(int(elem))

    for i in ids:
        for r in ranges:
            lo, hi = r
            if i >= lo and i <= hi:
                count += 1
                break
    
    print(count)


# Give 2 ranges [n, m] and [p, q]
# if we merge [n, m] into [p, q], then we have to do one
# of these things:
# 1. keep entirety of [n, m] (no overlap) -> m < p or n > q
# 2. discard [n, m] since its contained in [p, q] -> n > p and m < q
# 3. extend [p, q] to the left -> n < p and m > p
# 4. extend [p, q] to the right -> n < q and m > q
# note im omitting the case where [n, m] replaces [p, q] and i'll
# since this algo would extend right and left, since a left/right
# extends aren't mutually exclusive
# lastly, we'll sort by start so we can merge in one pass
# look at me writing out algos without getting paid
def consolidate_ranges(ranges):
    if not ranges:
        return []
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    p, q = ranges[0]

    for n, m in ranges[1:]:
        if m < p or n > q:
            merged.append((p, q))
            p, q = n, m
        else:
            if n >= p and m <= q:
                continue
            if n < p and m >= p:
                p = n
            if n <= q and m > q:
                q = m
    merged.append((p, q))
    return merged


def part2():
    arr = get_input()
    ranges = []
    count = 0

    for elem in arr[0]:
        lo, hi = elem.split("-")
        ranges.append((int(lo), int(hi)))

    collapsed_ranges = consolidate_ranges(ranges)
    
    for cr in collapsed_ranges:
        curr = cr[1] - cr[0] + 1
        count += curr

    print("Part 2 result: ", count)


part1()
part2()
