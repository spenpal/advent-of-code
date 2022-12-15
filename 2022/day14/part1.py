# IMPORTS
import ast
import re


# FUNCTIONS
def print_cave(cave):
    for row in cave:
        print("".join(row[450:550]))


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


def drop_sand(cave, pos):
    pos_x, pos_y = pos
    if pos_y == len(cave) - 1:  # have reached the abyss
        return pos

    if cave[pos_y + 1][pos_x] == ".":
        new_pos = (pos_x, pos_y + 1)
        return drop_sand(cave, new_pos)
    elif cave[pos_y + 1][pos_x - 1] == ".":
        new_pos = (pos_x - 1, pos_y + 1)
        return drop_sand(cave, new_pos)
    elif cave[pos_y + 1][pos_x + 1] == ".":
        new_pos = (pos_x + 1, pos_y + 1)
        return drop_sand(cave, new_pos)

    return pos


# MAIN
cave = [["."] * 1000 for _ in range(170)]
start = (500, 0)

with open("input.txt") as f:
    for line in f:
        coords = re.findall(r"\d+,\d+", line)
        coords = [ast.literal_eval(f"({coord})") for coord in coords]
        for i in range(1, len(coords)):
            add_rocks(cave, coords[i - 1], coords[i])

sand_num = 0
while all(space == "." for space in cave[-1]):
    sand_num += 1
    print(f"SAND #: {sand_num}")
    cave[start[1]][start[0]] = "O"
    print_cave(cave)

    final_pos = drop_sand(cave, start)
    cave[final_pos[1]][final_pos[0]] = "O"

    print("\n")

print("Units of Sand Before Falling to the Abyss:", sand_num - 1)
