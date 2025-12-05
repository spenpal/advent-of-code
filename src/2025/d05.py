from collections import deque


def parse(data: str) -> dict[int, tuple]:
    fresh_ranges, ingredient_ids = data.strip().split("\n\n")

    fresh_ranges = [
        tuple(map(int, range_str.split("-")))
        for range_str in fresh_ranges.strip().splitlines()
    ]

    ingredient_ids = [int(id_str) for id_str in ingredient_ids.strip().splitlines()]

    return {1: (fresh_ranges, ingredient_ids), 2: (fresh_ranges, ingredient_ids)}


def part1(fresh_ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    def is_fresh(ingredient_id: int) -> bool:
        """Check if an ingredient ID falls within any fresh range."""
        return any(start <= ingredient_id <= end for start, end in fresh_ranges)

    return sum(is_fresh(ingredient_id) for ingredient_id in ingredient_ids)


def part2(fresh_ranges: list[tuple[int, int]], _ingredient_ids: list[int]) -> int:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n).
    """  # noqa: D205, D212

    def is_overlap(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
        """Check if two ranges overlap."""
        return max(range1[0], range2[0]) <= min(range1[1], range2[1])

    def merge_ranges(
        range1: tuple[int, int],
        range2: tuple[int, int],
    ) -> tuple[int, int]:
        return (min(range1[0], range2[0]), max(range1[1], range2[1]))

    fresh_ranges_queue: deque[tuple[int, int]] = deque(sorted(fresh_ranges))
    index = 0

    while index < len(fresh_ranges_queue) - 1:
        range1, range2 = fresh_ranges_queue[index], fresh_ranges_queue[index + 1]
        if is_overlap(range1, range2):
            fresh_ranges_queue[index] = merge_ranges(range1, range2)
            del fresh_ranges_queue[index + 1]
        else:
            index += 1

    return sum(
        fresh_range[1] - fresh_range[0] + 1 for fresh_range in fresh_ranges_queue
    )
