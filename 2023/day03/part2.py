# IMPORTS
from collections import defaultdict

gears = defaultdict(list)


# FUNCTIONS
def check_for_gear(schematic, r, c1, c2, num):
    max_row, max_col = len(schematic) - 1, len(schematic[0]) - 1

    start_row, end_row = max(0, r - 1), min(max_row, r + 1)
    start_col, end_col = max(0, c1 - 1), min(max_col, c2 + 1)

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if schematic[row][col] == "*":
                gears[(row, col)].append(num)


# MAIN
with open("input") as f:
    schematic = [line.strip() for line in f]

r = 0
while r < len(schematic):
    c = 0
    while c < len(schematic[r]):
        if schematic[r][c].isdigit():
            first_digit_pos = c
            while c < len(schematic[r]) and schematic[r][c].isdigit():
                c += 1
            last_digit_pos = c - 1
            num = int("".join(schematic[r][first_digit_pos : last_digit_pos + 1]))
            check_for_gear(schematic, r, first_digit_pos, last_digit_pos, num)
            c = last_digit_pos + 1
        else:
            c += 1
    r += 1

gear_ratios = [
    part_nums[0] * part_nums[1] for part_nums in gears.values() if len(part_nums) == 2
]
print(sum(gear_ratios))
