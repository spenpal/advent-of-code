from collections import deque
from collections.abc import Generator

from src.types import Grid, Pair
from src.utils import out_of_bounds


def parse(data: str) -> dict[int, tuple]:
    data = [list(map(int, line.strip())) for line in data.strip().splitlines()]
    return {1: (data,), 2: (data,)}


def get_trailheads(top_map: Grid) -> list[Pair]:
    return [
        (row, col)
        for row in range(len(top_map))
        for col in range(len(top_map[row]))
        if top_map[row][col] == 0
    ]


def find_trailends(trailhead: Pair, top_map: Grid) -> list[Pair]:
    def get_valid_moves(row: int, col: int) -> Generator[Pair]:
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_row, next_col = row + dr, col + dc
            if (
                not out_of_bounds(rows, cols, next_row, next_col)
                and top_map[next_row][next_col] == top_map[row][col] + 1
            ):
                yield (next_row, next_col)

    rows, cols = len(top_map), len(top_map[0])

    queue = deque([trailhead])
    trailends = []

    while queue:
        position = queue.popleft()
        row, col = position
        if top_map[row][col] == 9:
            trailends.append(position)
        else:
            queue.extend(get_valid_moves(row, col))

    return trailends


def part1(top_map: Grid) -> int:
    trailheads = get_trailheads(top_map)
    return sum(len(set(find_trailends(trailhead, top_map))) for trailhead in trailheads)


def part2(top_map: Grid) -> int:
    trailheads = get_trailheads(top_map)
    return sum(len(find_trailends(trailhead, top_map)) for trailhead in trailheads)
