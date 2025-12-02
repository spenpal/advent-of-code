def parse(data: str) -> dict[int, tuple]:
    crabs = data.strip().split(",")
    crabs = list(map(int, crabs))
    return {1: (crabs,), 2: (crabs,)}


def explicit_sum(n):
    return (n * (n + 1)) // 2


def part1(crabs):
    crabs = [
        sum(abs(pos - crab) for crab in crabs)
        for pos in range(min(crabs), max(crabs) + 1)
    ]
    return min(crabs)


def part2(crabs):
    crabs = [
        sum(explicit_sum(abs(pos - crab)) for crab in crabs)
        for pos in range(min(crabs), max(crabs) + 1)
    ]
    return min(crabs)
