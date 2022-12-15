# IMPORTS
import ast
import re


# FUNCTIONS
def print_cave(cave):
    for row in cave:
        print("".join(row[250:750]))


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

    if cave[pos_y + 1][pos_x] == ".":
        cave[pos_y][pos_x] = "."
        cave[pos_y + 1][pos_x] = "O"
        new_pos = (pos_x, pos_y + 1)
        drop_sand(cave, new_pos)
    elif cave[pos_y + 1][pos_x - 1] == ".":
        cave[pos_y][pos_x] = "."
        cave[pos_y + 1][pos_x - 1] = "O"
        new_pos = (pos_x - 1, pos_y + 1)
        drop_sand(cave, new_pos)
    elif cave[pos_y + 1][pos_x + 1] == ".":
        cave[pos_y][pos_x] = "."
        cave[pos_y + 1][pos_x + 1] = "O"
        new_pos = (pos_x + 1, pos_y + 1)
        drop_sand(cave, new_pos)


# MAIN
floor_lvl = 167
cave = [["."] * 1000 for _ in range(floor_lvl)]
cave[-1] = ["#"] * 1000
start = (500, 0)

with open("input.txt") as f:
    for line in f:
        coords = re.findall(r"\d+,\d+", line)
        coords = [ast.literal_eval(f"({coord})") for coord in coords]
        for i in range(1, len(coords)):
            add_rocks(cave, coords[i - 1], coords[i])

sand_num = 0
while cave[start[1]][start[0]] != "O":
    sand_num += 1
    cave[start[1]][start[0]] = "O"
    drop_sand(cave, start)

print("Units of Sand Before Filling Up Completely:", sand_num)
