from collections import defaultdict


def parse(data: str) -> dict[int, tuple]:
    ordering, updates = data.strip().split("\n\n")

    ordering = [
        tuple(map(int, line.split("|"))) for line in ordering.strip().splitlines()
    ]
    ordering_map = defaultdict(set)
    for first, second in ordering:
        ordering_map[first].add(second)

    updates = [
        list(map(int, line.strip().split(","))) for line in updates.strip().splitlines()
    ]

    return {1: (ordering_map, updates), 2: (ordering_map, updates)}


def valid_update(ordering: dict[int, set[int]], update: list[int]) -> bool:
    return all(
        set(update[i + 1 :]).issubset(ordering[update[i]])
        for i in range(len(update) - 1)
    )


def part1(ordering: dict[int, set[int]], updates: list[list[int]]) -> int:
    valid_updates = [update for update in updates if valid_update(ordering, update)]
    return sum(update[len(update) // 2] for update in valid_updates)


def part2(ordering: dict[int, set[int]], updates: list[list[int]]) -> int:
    def order(page_num: int, update: list[int]) -> int:
        return len((set(update) - {page_num}) & ordering[page_num])

    invalid_updates = [
        update for update in updates if not valid_update(ordering, update)
    ]
    fixed_updates = [
        sorted(update, reverse=True, key=lambda num: order(num, update))
        for update in invalid_updates
    ]
    return sum(update[len(update) // 2] for update in fixed_updates)
