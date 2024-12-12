from collections.abc import Iterable, Sequence
from itertools import chain, zip_longest

from .types import Grid, Pair, T


class WordSearch:
    Position = Pair[int]
    Match = list[Position]
    Matches = list[Match]

    def __init__(
        self, grid: Grid[str] | Sequence[str], case_sensitive: bool = True
    ) -> None:
        if not all(len(row) == len(grid[0]) for row in grid):
            msg = "All rows in the grid must have the same length."
            raise ValueError(msg)
        self.grid = (
            grid if case_sensitive else [[c.lower() for c in row] for row in grid]
        )
        self.case_sensitive = case_sensitive
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.direction = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
            "UL": (-1, -1),
            "UR": (-1, 1),
            "DL": (1, -1),
            "DR": (1, 1),
        }

    def _valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def _get_matches(self, row: int, col: int, target_word: str) -> Matches:
        matches = []
        for row_step, col_step in self.direction.values():
            positions = [
                (row + row_step * i, col + col_step * i)
                for i in range(len(target_word))
            ]
            word = "".join(
                self.grid[r][c] if self._valid_position(r, c) else ""
                for r, c in positions
            )
            if word == target_word:
                matches.append(positions)
        return matches

    def search(self, word: str, find_all: bool = False) -> Match | Matches:
        if not word:
            return []

        target_word = word if self.case_sensitive else word.lower()
        matches = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == target_word[0]:
                    matches.extend(self._get_matches(row, col, target_word))
                    if not find_all and len(matches):
                        return matches[0]
        return matches


def manhattan_distance(p1: Pair[int], p2: Pair[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def merge(iterable1: Iterable[T], iterable2: Iterable[T]) -> list[T]:
    """Alternates elements from two iterables into a single list, appending remaining elements from the longer iterable."""
    merged_iterable = chain.from_iterable(zip_longest(iterable1, iterable2))
    return [item for item in merged_iterable if item is not None]


def out_of_bounds(row_len: int, col_len: int, row: int, col: int) -> bool:
    return not (0 <= row < row_len and 0 <= col < col_len)
