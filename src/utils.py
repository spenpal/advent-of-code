from collections.abc import Hashable, Iterable, Sequence
from itertools import chain, zip_longest

from .type_defs import Grid, Pair, T, TComparable


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
            grid if case_sensitive else [[char.lower() for char in row] for row in grid]
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
                (row + row_step * offset, col + col_step * offset)
                for offset in range(len(target_word))
            ]
            word = "".join(
                self.grid[row_idx][col_idx]
                if self._valid_position(row_idx, col_idx)
                else ""
                for row_idx, col_idx in positions
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


def manhattan_distance(point1: Pair[int], point2: Pair[int]) -> int:
    """Calculate the Manhattan distance between two points.

    Args:
        point1: The first point as a (row, col) pair.
        point2: The second point as a (row, col) pair.

    Returns:
        The Manhattan distance between the two points.
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def euclidean_distance(point1: tuple[int, ...], point2: tuple[int, ...]) -> float:
    """Calculate the Euclidean distance between two points in n-dimensional space.

    Args:
        point1: The first point as a sequence of coordinates.
        point2: The second point as a sequence of coordinates.

    Returns:
        The Euclidean distance between the two points.

    Raises:
        ValueError: If the points have different dimensions.
    """
    if len(point1) != len(point2):
        msg = "Points must have the same number of dimensions."
        raise ValueError(msg)
    return sum((a - b) ** 2 for a, b in zip(point1, point2, strict=True)) ** 0.5


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
    value: int,
    min_val: int,
    max_val: int,
    step: int = 1,
) -> tuple[int, int]:
    """Calculate a new value by stepping and wrapping within a range.

    Steps from the current value by the specified step amount, wrapping
    around if the result exceeds the bounds [min_val, max_val].

    Args:
        value: The current value.
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
    offset = value - min_val + step
    wrap_count, remainder = divmod(offset, range_size)
    new_val = min_val + remainder
    return new_val, wrap_count


def factors(number: int) -> list[int]:
    """Find all factors of a number.

    Args:
        number: The number to find the factors of.

    Returns:
        A list of all factors of the number (sorted in ascending order)

    Time Complexity:
        O(sqrt(n) + k log k), where k is the number of factors found.
        The main loop runs in O(sqrt(n)), and the final sort of the list
        of factors is O(k log k).
    """
    if number < 1:
        return []
    factors_list: list[int] = []
    for factor in range(1, int(number**0.5) + 1):
        if number % factor == 0:
            factors_list.append(factor)
            complement_factor = number // factor
            if complement_factor != factor:
                factors_list.append(complement_factor)
    return sorted(factors_list)


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

    for part_index in range(parts):
        size = base + (1 if part_index < extra else 0)
        end = start + size
        substrings.append(string[start:end])
        start = end

    return substrings


def max_with_index(iterable: Iterable[TComparable]) -> tuple[int, TComparable]:
    """Returns the maximum value and its index in an iterable.

    Args:
        iterable: The iterable to find the maximum value of.

    Returns:
        A tuple of (index, value) where index is the position of the maximum value.
    """
    max_value: TComparable | None = None
    max_index = -1
    for index, value in enumerate(iterable):
        if max_value is None or value > max_value:
            max_value = value
            max_index = index
    if max_value is None:
        msg = "max_with_index() arg is an empty sequence"
        raise ValueError(msg)
    return (max_index, max_value)


def transpose(
    grid: Grid[T],
    fillvalue: T | None = None,
) -> list[list[T | None]]:
    """Transpose a 2D array (rows become columns and columns become rows).

    Handles irregular grids by padding shorter rows with fillvalue.

    Args:
        grid: A 2D grid to transpose. Rows can have different lengths.
        fillvalue: Value to use for missing elements when rows have different
            lengths. Defaults to None. If None, None values are filtered out
            from the result.

    Returns:
        A new grid where rows and columns are swapped. If fillvalue is None,
        None values are filtered out, resulting in columns of varying lengths.

    Example:
        [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]
        [['3', '2', '1'], ['5', '4'], ['6']] ->
        [['3', '5', '6'], ['2', '4'], ['1']]
    """
    if not grid:
        return []
    transposed = [list(col) for col in zip_longest(*grid, fillvalue=fillvalue)]
    if fillvalue is None:
        return [[item for item in col if item is not None] for col in transposed]
    return transposed


def all_same(iterable: Iterable[T], value: T | None = None) -> bool:
    """Check if all values in an iterable are the same.

    Stops as soon as it finds a different value,
    without needing to consume the entire iterable.

    Args:
        iterable: The iterable to check.
        value: Optional specific value to check against. If provided,
            checks if all values equal this value. If not provided,
            checks if all values are equal to each other.

    Returns:
        True if all values are the same (or equal to the provided value)
        or if the iterable is empty, False otherwise.

    Examples:
        >>> all_same([1, 1, 1, 1])
        True
        >>> all_same([1, 2, 1])
        False
        >>> all_same([])
        True
        >>> all_same(["a", "a", "a"])
        True
        >>> all_same([1, 1, 1], 1)
        True
        >>> all_same([1, 1, 1], 2)
        False
    """
    iterator = iter(iterable)

    if value is not None:
        # Check if all values equal the provided value
        return all(item == value for item in iterator)

    try:
        first_value = next(iterator)
    except StopIteration:
        # Empty iterable - considered all same
        return True

    return all(item == first_value for item in iterator)


class DisjointSet[TElement: Hashable]:
    """Efficient Disjoint Set Union (Union-Find) data structure for any hashable type.

    Uses path compression and union by size for near-constant time operations.
    Time complexity: O(α(n)) amortized per operation, where α is the inverse
    Ackermann function (effectively constant for all practical values of n).

    Example with integers:
        >>> ds = DisjointSet(5)  # Creates sets {0}, {1}, {2}, {3}, {4}
        >>> ds.union(0, 1)
        >>> ds.connected(0, 1)
        True

    Example with strings:
        >>> ds = DisjointSet(["alice", "bob", "charlie"])
        >>> ds.union("alice", "bob")
        >>> ds.connected("alice", "bob")
        True
        >>> ds.size("alice")
        2

    Example with tuples (coordinates):
        >>> ds = DisjointSet([(0, 0), (0, 1), (1, 0)])
        >>> ds.union((0, 0), (0, 1))
        >>> ds.connected((0, 0), (1, 0))
        False
    """  # noqa: RUF002

    def __init__(self, elements: int | Iterable[TElement] | None = None) -> None:
        """Initialize disjoint sets from elements.

        Args:
            elements: Can be:
                - An integer n: creates sets for elements 0, 1, ..., n-1
                - An iterable: creates one set for each unique element
                - None: creates empty structure (use make_set to add elements)
        """
        self.parent: dict[TElement, TElement] = {}
        self.rank: dict[TElement, int] = {}
        self.set_size: dict[TElement, int] = {}
        self.count = 0

        if elements is not None:
            if isinstance(elements, int):
                # For backward compatibility: integer creates sets 0..n-1
                elements = range(elements)  # type: ignore[assignment]

            for element in elements:  # type: ignore[union-attr]
                self.make_set(element)

    def make_set(self, x: TElement) -> None:
        """Create a new set containing only element x.

        If x already exists, does nothing.

        Args:
            x: The element to create a set for.
        """
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.set_size[x] = 1
            self.count += 1

    def find(self, x: TElement) -> TElement:
        """Find the representative (root) of the set containing x.

        Uses path compression: all nodes along the path to root point directly
        to root after this operation, speeding up future queries.

        Args:
            x: The element to find the representative of.

        Returns:
            The representative of the set containing x.

        Raises:
            KeyError: If x is not in any set.
        """
        if x not in self.parent:
            msg = f"Element {x} is not in any set"
            raise KeyError(msg)

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: TElement, y: TElement) -> bool:
        """Merge the sets containing x and y.

        Uses union by rank: attaches the tree with lower rank to the root
        of the tree with higher rank, keeping trees balanced.

        Args:
            x: Element in the first set.
            y: Element in the second set.

        Returns:
            True if sets were merged (x and y were in different sets),
            False if they were already in the same set.

        Raises:
            KeyError: If x or y is not in any set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.set_size[root_x] += self.set_size[root_y]

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: TElement, y: TElement) -> bool:
        """Check if x and y are in the same set.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if x and y are in the same set, False otherwise.

        Raises:
            KeyError: If x or y is not in any set.
        """
        return self.find(x) == self.find(y)

    def size(self, x: TElement) -> int:
        """Get the size of the set containing x.

        Args:
            x: The element whose set size to find.

        Returns:
            The number of elements in the set containing x.

        Raises:
            KeyError: If x is not in any set.
        """
        return self.set_size[self.find(x)]

    def get_sets(self) -> dict[TElement, list[TElement]]:
        """Get all disjoint sets as a dictionary.

        Returns:
            A dictionary mapping each representative to the list of elements
            in that set.
        """
        sets: dict[TElement, list[TElement]] = {}
        for element in self.parent:
            root = self.find(element)
            if root not in sets:
                sets[root] = []
            sets[root].append(element)
        return sets

    def __contains__(self, x: TElement) -> bool:
        """Check if element x is in the structure.

        Args:
            x: The element to check.

        Returns:
            True if x is in any set, False otherwise.
        """
        return x in self.parent

    def __len__(self) -> int:
        """Return the number of disjoint sets.

        Returns:
            The number of disjoint sets.
        """
        return self.count
