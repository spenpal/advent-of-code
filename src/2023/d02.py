import math
from collections import defaultdict


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


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


def part1(data):
    id_sum = 0

    for line in data:
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

    return id_sum


def part2(data):
    sum_of_powers = 0

    for line in data:
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

    return sum_of_powers
