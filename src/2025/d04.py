from src.type_defs import Grid, Pair
from src.utils import out_of_bounds

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}

ROLL = "@"
EMPTY = "."
MAX_ADJACENT_ROLLS = 3


def parse(data: str) -> dict[int, tuple]:
    grid = [list(line.strip()) for line in data.strip().splitlines()]
    return {1: (grid,), 2: (grid,)}


def is_accessible(grid: Grid[str], position: Pair) -> bool:
    """Check if a roll can be accessed by a forklift."""
    row, col = position
    adjacent_rolls = 0

    for dr, dc in DIRECTIONS.values():
        neighbor_row, neighbor_col = row + dr, col + dc

        if (
            not out_of_bounds(len(grid), len(grid[0]), neighbor_row, neighbor_col)
            and grid[neighbor_row][neighbor_col] == ROLL
        ):
            adjacent_rolls += 1

    return adjacent_rolls <= MAX_ADJACENT_ROLLS


def part1(grid: Grid[str]) -> int:
    accessible_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ROLL and is_accessible(grid, (row, col)):
                accessible_count += 1

    return accessible_count


def part2(grid: Grid[str]) -> int:
    def no_changes(old_grid: Grid[str], new_grid: Grid[str]) -> bool:
        """Check if two grids are identical (no rolls were removed)."""
        return all(
            old_grid[i][j] == new_grid[i][j]
            for i in range(len(old_grid))
            for j in range(len(old_grid[0]))
        )

    rolls_removed = 0

    while True:
        prev_grid = [row[:] for row in grid]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ROLL and is_accessible(grid, (row, col)):
                    grid[row][col] = EMPTY
                    rolls_removed += 1

        if no_changes(prev_grid, grid):
            break

    return rolls_removed
