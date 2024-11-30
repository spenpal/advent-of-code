import ast
import re


def add_rocks(cave, r1, r2):
    if r1[0] == r2[0]:
        rock_x = r1[0]
        rocks_y = range(min(r1[1], r2[1]), max(r1[1], r2[1]) + 1)
        rocks = [(rock_x, rock_y) for rock_y in rocks_y]
    else:
        rock_y = r1[1]
        rocks_x = range(min(r1[0], r2[0]), max(r1[0], r2[0]) + 1)
        rocks = [(rock_x, rock_y) for rock_x in rocks_x]

    for x, y in rocks:
        cave[y][x] = "#"


def parse(data: str) -> dict[int, tuple]:
    cave1 = [["."] * 1000 for _ in range(170)]
    cave2 = [["."] * 1000 for _ in range(167)]
    cave2[-1] = ["#"] * 1000

    for line in data.strip().splitlines():
        coords = re.findall(r"\d+,\d+", line)
        coords = [ast.literal_eval(f"({coord})") for coord in coords]
        for i in range(1, len(coords)):
            add_rocks(cave1, coords[i - 1], coords[i])
            add_rocks(cave2, coords[i - 1], coords[i])

    return {1: (cave1,), 2: (cave2,)}


def print_cave(cave):
    for row in cave:
        print("".join(row[450:550]))


def drop_sand(cave, pos):
    pos_x, pos_y = pos
    if pos_y == len(cave) - 1:  # have reached the abyss
        return pos

    if cave[pos_y + 1][pos_x] == ".":
        new_pos = (pos_x, pos_y + 1)
        return drop_sand(cave, new_pos)
    if cave[pos_y + 1][pos_x - 1] == ".":
        new_pos = (pos_x - 1, pos_y + 1)
        return drop_sand(cave, new_pos)
    if cave[pos_y + 1][pos_x + 1] == ".":
        new_pos = (pos_x + 1, pos_y + 1)
        return drop_sand(cave, new_pos)

    return pos


def part1(cave):
    sand_num = 0
    start = (500, 0)

    while all(space == "." for space in cave[-1]):
        sand_num += 1
        print(f"SAND #: {sand_num}")
        cave[start[1]][start[0]] = "O"
        print_cave(cave)

        final_pos = drop_sand(cave, start)
        cave[final_pos[1]][final_pos[0]] = "O"

        print("\n")

    return sand_num - 1


def part2(cave):
    start = (500, 0)
    sand_num = 0

    while cave[start[1]][start[0]] != "O":
        sand_num += 1
        final_pos = drop_sand(cave, start)
        cave[final_pos[1]][final_pos[0]] = "O"

    return sand_num
