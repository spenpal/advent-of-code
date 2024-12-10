from collections import defaultdict
from itertools import combinations

from src.types import Pair
from src.utils import out_of_bounds


def parse(data: str) -> dict[int, tuple]:
    data = [line.strip() for line in data.strip().splitlines()]
    grid_dims = len(data), len(data[0])

    antennas = defaultdict(set)
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != ".":
                antennas[char].add((row, col))

    return {1: (antennas, grid_dims), 2: (antennas, grid_dims)}


def part1(antennas: defaultdict[str, set[Pair]], grid_dims: Pair) -> int:
    antinodes = set()

    for positions in antennas.values():
        for pos_1, pos_2 in combinations(positions, 2):
            slope = (pos_2[0] - pos_1[0], pos_2[1] - pos_1[1])
            antinode_1 = pos_1[0] - slope[0], pos_1[1] - slope[1]
            antinode_2 = pos_2[0] + slope[0], pos_2[1] + slope[1]

            antinodes.update(
                antinode
                for antinode in (antinode_1, antinode_2)
                if not out_of_bounds(*grid_dims, *antinode)
            )

    return len(antinodes)


def part2(antennas: defaultdict[str, set[Pair]], grid_dims: Pair) -> int:
    antinodes = set()

    for positions in antennas.values():
        for pos_1, pos_2 in combinations(positions, 2):
            slope = (pos_2[0] - pos_1[0], pos_2[1] - pos_1[1])
            antinode_1 = pos_1[0] - slope[0], pos_1[1] - slope[1]
            antinode_2 = pos_1[0] + slope[0], pos_1[1] + slope[1]

            antinodes_1, antinodes_2 = set(), set()
            while not out_of_bounds(*grid_dims, *antinode_1):
                antinodes_1.add(antinode_1)
                antinode_1 = antinode_1[0] - slope[0], antinode_1[1] - slope[1]
            while not out_of_bounds(*grid_dims, *antinode_2):
                antinodes_2.add(antinode_2)
                antinode_2 = antinode_2[0] + slope[0], antinode_2[1] + slope[1]

            antinodes.update(antinodes_1 | antinodes_2)

    return len(antinodes | set.union(*antennas.values()))
