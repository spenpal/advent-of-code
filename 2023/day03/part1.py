# IMPORTS
import re


# FUNCTIONS
def check_part_number(schematic, r, c1, c2):
    """
    Example

                <top>    .....
                <side>   .633.  <side>
                <bottom> ..#..

    Make sure to account for the edges of the schematic
    Example

                        633.%
                        .5...
    """
    max_row, max_col = len(schematic) - 1, len(schematic[0]) - 1

    start_row, end_row = max(0, r - 1), min(max_row, r + 1)
    start_col, end_col = max(0, c1 - 1), min(max_col, c2 + 1)

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if re.match(r"[^\.0-9]", schematic[row][col]):
                return True

    return False


# MAIN
with open("input") as f:
    schematic = [line.strip() for line in f]

part_nums = []

r = 0
while r < len(schematic):
    c = 0
    while c < len(schematic[r]):
        if schematic[r][c].isdigit():
            first_digit_pos = c
            while c < len(schematic[r]) and schematic[r][c].isdigit():
                c += 1
            last_digit_pos = c - 1
            if check_part_number(schematic, r, first_digit_pos, last_digit_pos):
                part_nums.append(
                    int("".join(schematic[r][first_digit_pos : last_digit_pos + 1]))
                )
            c = last_digit_pos + 1
        else:
            c += 1
    r += 1

print(sum(part_nums))
