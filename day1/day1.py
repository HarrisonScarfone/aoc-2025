"""
TIL: If -250 // 2 in python is not 2.
"""

def read_input():
    with open("C:\\Users\\harry\\Desktop\\aoc2025\\day1\\input_p1.txt", "r") as f:
        return [elem.strip() for elem in f.readlines()]

def rotate(state, instruction):
    direction, magnitude = instruction[0], int(instruction[1:])
    zero_count = 0

    if direction == "R":
        new_state = (100 - state) % 100
        new_state = 100 if new_state == 0 else new_state

        if new_state <= magnitude:
            zero_count = 1 + (magnitude - new_state) // 100
            
        new_state = (state + magnitude) % 100
    else:
        new_state = 100 if state == 0 else state
        if new_state <= magnitude:
            zero_count = 1 + (magnitude - new_state) // 100

        new_state = (state - magnitude) % 100
    
    return new_state, zero_count
    
def crack_safe():
    instructions = read_input()
    state, p2_zero_count = 50, 0

    p1_password = 0
    p2_password = 0
    
    for instruction in instructions:
        state, p2_zero_count = rotate(state, instruction)
        p1_password += 1 if not state else 0
        p2_password += p2_zero_count

    print("Part 1 password is: ", p1_password)
    print("Part 2 password is: ", p2_password)

crack_safe()
