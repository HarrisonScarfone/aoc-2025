FILEPATH = "C:\\Users\\harry\\Desktop\\aoc2025\\day6\\input.txt"

def get_input(fp=FILEPATH):
    arr = []
    with open(fp, "r") as f:
        for elem in f.readlines():
            l = (elem.strip().split(" "))
            arr.append([elem for elem in l if elem != ""])
    arr, signs = arr[:-1], arr[-1]
    arr = [[int(v) for v in elem] for elem in arr]
    return (arr, signs)


def part1():
    arr, signs = get_input()
    sol = [0 if sign == "+" else 1 for sign in signs]
    
    for nums in arr:
        for i, num in enumerate(nums):
            if signs[i] == "*":
                sol[i] *= num
            else:
                sol[i] += num

    print("Part 1 result: ", sum(sol))


def get_input_p2(fp=FILEPATH):
    arr = []
    with open(fp, "r") as f:
        for elem in f.readlines():
            l = (elem.rstrip("\n"))
            arr.append(l)
    arr, signs = arr[:-1], arr[-1]
    return (arr, signs)

def part2():
    arr, signs = get_input_p2()
    signs = [elem for elem in [elem.strip() for elem in signs.split(" ")] if elem]   

    col = []
    cols = []

    for i in range(len(arr[0])):
        curr_num = ""

        for row in arr:
            curr_num += row[i]

        curr_num = curr_num.strip()

        if not curr_num:
            cols.append(col)
            col = []
        else:
            col.append(curr_num)
    
    cols.append(col)
    result = 0
    for elem in cols:
        curr_nums = [int(numstr) for numstr in elem]
        sign = signs.pop(0)
        if sign == "*":
            res = 1
            for num in curr_nums:
                res *= num 
            result += res
        else:
            res = sum(curr_nums)
            result += res

    print("Part 2 result: ", result)


part1()
part2()
