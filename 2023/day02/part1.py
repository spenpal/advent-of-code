# IMPORTS
from collections import defaultdict


# FUNCTIONS
def check(cubes):
    max_cube_count = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for color, count in cubes.items():
        if count > max_cube_count[color]:
            return False

    return True


# MAIN
with open("input") as f:
    id_sum = 0

    for line in f:
        max_color_cubes = defaultdict(int)

        game, sets = line.strip().split(": ")
        game_id = int(game.split(" ")[1])
        sets = sets.split("; ")

        for set in sets:
            cubes = set.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                max_color_cubes[color] = max(max_color_cubes[color], int(count))

        if check(max_color_cubes):
            id_sum += game_id

    print(id_sum)
