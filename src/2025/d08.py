from itertools import combinations
from math import prod

from src.type_defs import Coord3D
from src.utils import DisjointSet, euclidean_distance

MAX_CONNECTIONS_EXAMPLE = 10
MAX_CONNECTIONS_PUZZLE = 1000
EXAMPLE_SIZE_THRESHOLD = 20


def parse(data: str) -> dict[int, tuple]:
    coordinates = [
        tuple(map(int, line.split(","))) for line in data.strip().splitlines()
    ]
    return {1: (coordinates,), 2: (coordinates,)}


def part1(coordinates: list[Coord3D]) -> float:
    # Calculate distances between all pairs, sorted by distance
    pairs_by_distance = sorted(
        [
            (euclidean_distance(coord1, coord2), coord1, coord2)
            for coord1, coord2 in combinations(coordinates, 2)
        ],
        key=lambda x: x[0],
    )

    # Track which junction boxes are in the same circuit
    circuits = DisjointSet(coordinates)

    # Connect the N closest pairs (10 for examples, 1000 for puzzle)
    is_example = len(coordinates) <= EXAMPLE_SIZE_THRESHOLD
    num_connections = MAX_CONNECTIONS_EXAMPLE if is_example else MAX_CONNECTIONS_PUZZLE

    for _, coord1, coord2 in pairs_by_distance[:num_connections]:
        circuits.union(coord1, coord2)

    # Return product of three largest circuits
    return prod(
        len(circuit)
        for circuit in sorted(circuits.get_sets().values(), key=len, reverse=True)[:3]
    )


def part2(coordinates: list[Coord3D]) -> int:
    # Calculate distances between all pairs, sorted by distance
    pairs_by_distance = sorted(
        [
            (euclidean_distance(coord1, coord2), coord1, coord2)
            for coord1, coord2 in combinations(coordinates, 2)
        ],
        key=lambda x: x[0],
    )

    # Track which junction boxes are in the same circuit
    circuits = DisjointSet(coordinates)

    # Keep connecting closest pairs until all are in one circuit
    for _, coord1, coord2 in pairs_by_distance:
        circuits.union(coord1, coord2)

        # Stop when all junction boxes connected
        if circuits.size(coord1) == len(coordinates):
            break

    # Return product of X coordinates of final connection
    return coord1[0] * coord2[0]
