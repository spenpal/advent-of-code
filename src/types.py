from collections.abc import Sequence
from typing import Any, TypeVar

T = TypeVar("T")

Pair = tuple[Any, Any]
Pairs = list[Pair]

Grid = Sequence[Sequence[T]]
