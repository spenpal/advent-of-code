from collections.abc import Iterator, Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


class OrderedSet(Generic[T]):
    def __init__(self) -> None:
        self._data: dict[T, None] = {}

    def add(self, value: T) -> None:
        self._data[value] = None

    def discard(self, value: T) -> None:
        self._data.pop(value, None)

    def __contains__(self, value: T) -> bool:
        return value in self._data

    def __iter__(self) -> Iterator[T]:
        return iter(self._data.keys())

    def __len__(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()

    def update(self, *values: T) -> None:
        for value in values:
            self.add(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderedSet):
            return False
        return list(self._data.keys()) == list(other._data.keys())

    def __repr__(self) -> str:
        return f"OrderedSet({list(self._data.keys())})"


class WordSearch:
    Position = tuple[int, int]
    Match = list[Position]
    Matches = list[Match]

    def __init__(
        self, grid: Sequence[Sequence[str]] | Sequence[str], case_sensitive: bool = True
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


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
