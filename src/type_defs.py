from typing import Protocol, Self, TypeVar


class Comparable(Protocol):
    """Protocol for types that support comparison operators."""

    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...


T = TypeVar("T")
TComparable = TypeVar("TComparable", bound=Comparable)

Pair = tuple[T, T]
Pairs = list[Pair]

Grid = list[list[T]]
