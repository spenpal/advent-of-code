def parse(data: str) -> dict[int, tuple]:
    data = [map(int, line.split()) for line in data.strip().splitlines()]
    ids_1, ids_2 = map(sorted, zip(*data, strict=False))
    return {1: (ids_1, ids_2), 2: (ids_1, ids_2)}


def part1(ids_1: list[int], ids_2: list[int]) -> int:
    return sum(abs(id_1 - id_2) for id_1, id_2 in zip(ids_1, ids_2, strict=False))


def part2(ids_1: list[int], ids_2: list[int]) -> int:
    return sum(id_1 * ids_2.count(id_1) for id_1 in ids_1)
