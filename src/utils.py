from collections.abc import Iterable, Sequence
from itertools import chain, zip_longest

from .type_defs import Grid, Pair, T


class WordSearch:
    """A word search solver for finding words in a 2D grid.

    Supports searching in 8 directions: up, down, left, right, and all four diagonals.
    Can perform case-sensitive or case-insensitive searches.
    """

    Position = Pair[int]
    Match = list[Position]
    Matches = list[Match]

    def __init__(
        self,
        grid: Grid[str] | Sequence[str],
        case_sensitive: bool = True,
    ) -> None:
        """Initialize a WordSearch instance.

        Args:
            grid: A 2D grid of characters. All rows must have the same length.
            case_sensitive: Whether the search should be case-sensitive.
                Defaults to True.

        Raises:
            ValueError: If not all rows in the grid have the same length.
        """
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
        """Check if a position is within the grid bounds.

        Args:
            row: The row index to check.
            col: The column index to check.

        Returns:
            True if the position is within bounds, False otherwise.
        """
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def _get_matches(self, row: int, col: int, target_word: str) -> Matches:
        """Find all matches of a word starting at a given position.

        Searches in all 8 directions from the starting position.

        Args:
            row: The starting row index.
            col: The starting column index.
            target_word: The word to search for.

        Returns:
            A list of matches, where each match is a list of positions forming the word.
        """
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
        """Search for a word in the grid.

        Args:
            word: The word to search for.
            find_all: If True, returns all matches. If False, returns only the
                first match. Defaults to False.

        Returns:
            If find_all is False, returns a single Match (list of positions)
                or empty list.
            If find_all is True, returns a list of all Matches found.
        """
        if not word:
            return []

        target_word = word if self.case_sensitive else word.lower()
        matches = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == target_word[0]:
                    matches.extend(self._get_matches(row, col, target_word))
                    if not find_all and matches:
                        return matches[0]
        return matches


def manhattan_distance(p1: Pair[int], p2: Pair[int]) -> int:
    """Calculate the Manhattan distance between two points.

    Args:
        p1: The first point as a (row, col) pair.
        p2: The second point as a (row, col) pair.

    Returns:
        The Manhattan distance between the two points.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def merge(iterable1: Iterable[T], iterable2: Iterable[T]) -> list[T]:
    """Alternate elements from two iterables into a single list.

    Takes elements from iterable1 and iterable2 alternately, appending
    remaining elements from the longer iterable if the lengths differ.

    Args:
        iterable1: The first iterable to merge.
        iterable2: The second iterable to merge.

    Returns:
        A list containing alternating elements from both iterables.
    """
    merged_iterable = chain.from_iterable(zip_longest(iterable1, iterable2))
    return [item for item in merged_iterable if item is not None]


def out_of_bounds(row_len: int, col_len: int, row: int, col: int) -> bool:
    """Check if a position is out of bounds for a grid of given dimensions.

    Args:
        row_len: The number of rows in the grid.
        col_len: The number of columns in the grid.
        row: The row index to check.
        col: The column index to check.

    Returns:
        True if the position is out of bounds, False otherwise.
    """
    return not (0 <= row < row_len and 0 <= col < col_len)


def wrap_step(
    *,
    val: int,
    min_val: int,
    max_val: int,
    step: int = 1,
) -> tuple[int, int]:
    """Calculate a new value by stepping and wrapping within a range.

    Steps from the current value by the specified step amount, wrapping
    around if the result exceeds the bounds [min_val, max_val].

    Args:
        val: The current value.
        min_val: The minimum value in the range (inclusive).
        max_val: The maximum value in the range (inclusive).
        step: The step amount to add. Defaults to 1.

    Returns:
        A tuple of (new_value, wrap_count) where:
        - new_value: The new value after stepping and wrapping within the range.
        - wrap_count: The number of times the value wrapped around the range.
          Positive for forward wraps, negative for backward wraps.
    """
    range_size = max_val - min_val + 1
    offset = val - min_val + step
    wrap_count, remainder = divmod(offset, range_size)
    new_val = min_val + remainder
    return new_val, wrap_count


def factors(n: int) -> list[int]:
    """Find all factors of a number.

    Args:
        n: The number to find the factors of.

    Returns:
        A list of all factors of the number (sorted in ascending order)

    Time Complexity:
        O(sqrt(n) + k log k), where k is the number of factors found.
        The main loop runs in O(sqrt(n)), and the final sort of the list
        of factors is O(k log k).
    """
    if n < 1:
        return []
    factors: list[int] = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if (j := n // i) != i:
                factors.append(j)
    return sorted(factors)


def split_string(string: str, parts: int) -> list[str]:
    """Split `string` into `parts` substrings whose lengths differ by at most 1.

    Example:
        string = "abcdefgh", parts = 3  ->  ['abc', 'def', 'gh']
        string = "abcdefgh", parts = 4  ->  ['ab', 'cd', 'ef', 'gh']

    Args:
        string: The string to split.
        parts: The number of parts to split the string into.

    Returns:
        A list of substrings.
    """
    if parts <= 0:
        msg = "Parts must be positive."
        raise ValueError(msg)

    base, extra = divmod(len(string), parts)

    substrings: list[str] = []
    start = 0

    for i in range(parts):
        size = base + (1 if i < extra else 0)
        end = start + size
        substrings.append(string[start:end])
        start = end

    return substrings
