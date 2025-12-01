import re
from collections import defaultdict


def parse(data: str) -> dict[int, tuple]:
    schematic = [line.strip() for line in data.splitlines()]
    return {1: (schematic,), 2: (schematic,)}


def part1(schematic):
    def check_part_number(schematic, r, c1, c2):
        """Example:
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
                    part_nums.append(int("".join(schematic[r][first_digit_pos : last_digit_pos + 1])))
                c = last_digit_pos + 1
            else:
                c += 1
        r += 1

    return sum(part_nums)


def part2(schematic):
    def check_for_gear(schematic, r, c1, c2, num):
        max_row, max_col = len(schematic) - 1, len(schematic[0]) - 1

        start_row, end_row = max(0, r - 1), min(max_row, r + 1)
        start_col, end_col = max(0, c1 - 1), min(max_col, c2 + 1)

        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if schematic[row][col] == "*":
                    gears[(row, col)].append(num)

    r = 0
    gears = defaultdict(list)
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

    gear_ratios = [part_nums[0] * part_nums[1] for part_nums in gears.values() if len(part_nums) == 2]
    return sum(gear_ratios)
