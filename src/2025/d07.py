from functools import cache

from src.type_defs import Grid, Pair
from src.utils import out_of_bounds

# Manifold symbols
SPLITTER = "^"
START = "S"
EMPTY = "."


def parse(data: str) -> dict[int, tuple]:
    grid = [list(line.strip()) for line in data.strip().splitlines()]
    return {1: (grid,), 2: (grid,)}


def part1(grid: Grid[str]) -> int:
    row_count, col_count = len(grid), len(grid[0])
    seen_positions: set[Pair[int]] = set()

    def get_beam_split_count(position: Pair[int]) -> int:
        """Count splits, tracking seen positions to avoid duplicates."""
        if position in seen_positions:
            return 0
        seen_positions.add(position)

        row_idx, col_idx = position
        if out_of_bounds(row_count, col_count, row_idx, col_idx):
            return 0

        if grid[row_idx][col_idx] == SPLITTER:
            return (
                1  # Count this split
                + get_beam_split_count((row_idx, col_idx - 1))  # Left beam
                + get_beam_split_count((row_idx, col_idx + 1))  # Right beam
            )

        return get_beam_split_count((row_idx + 1, col_idx))  # Down beam

    start_pos = (0, grid[0].index(START))
    return get_beam_split_count(start_pos)


def part2(grid: Grid[str]) -> int:
    row_count, col_count = len(grid), len(grid[0])

    @cache
    def get_timeline_count(position: Pair[int]) -> int:
        """Count timelines created by a single quantum particle."""
        row_idx, col_idx = position

        if out_of_bounds(row_count, col_count, row_idx, col_idx):
            return 1  # Particle exits manifold: one complete timeline

        if grid[row_idx][col_idx] == SPLITTER:
            return (
                get_timeline_count((row_idx, col_idx - 1))  # Left timeline(s)
                + get_timeline_count((row_idx, col_idx + 1))  # Right timeline(s)
            )

        # Continue downward in current timeline
        return get_timeline_count((row_idx + 1, col_idx))

    start_pos = (0, grid[0].index(START))
    return get_timeline_count(start_pos)
