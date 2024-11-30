def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    complete_overlap_pairs = 0
    for line in data:
        elf1, elf2 = line.strip().split(",")
        elf1 = tuple(map(int, elf1.split("-")))
        elf2 = tuple(map(int, elf2.split("-")))

        overlap = (max(elf1[0], elf2[0]), min(elf1[1], elf2[1]))
        complete_overlap_pairs += overlap == elf1 or overlap == elf2
    return complete_overlap_pairs


def part2(data):
    overlap_pairs = 0
    for line in data:
        elf1, elf2 = line.strip().split(",")
        elf1 = tuple(map(int, elf1.split("-")))
        elf2 = tuple(map(int, elf2.split("-")))

        overlap = (max(elf1[0], elf2[0]), min(elf1[1], elf2[1]))
        overlap_pairs += overlap[0] <= overlap[1]
    return overlap_pairs
