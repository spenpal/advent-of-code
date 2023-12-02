# IMPORTS
import math
from collections import defaultdict

# MAIN
with open("input") as f:
    sum_of_powers = 0

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

        sum_of_powers += math.prod(max_color_cubes.values())

    print(sum_of_powers)
