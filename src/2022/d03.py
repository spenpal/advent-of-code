import string
from itertools import islice

priority = {
    let: p + 1 for p, let in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    priority_sum = 0
    for line in data:
        rucksack = line.strip()
        compartments = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
        common_item_type = list(set(compartments[0]) & set(compartments[1]))[0]
        priority_sum += priority[common_item_type]
    return priority_sum


def part2(data):
    priority_sum = 0
    while elf_group := list(islice(data, 3)):
        print(elf_group)
        common_item_type = list(
            set.intersection(*[set(rucksack.strip()) for rucksack in elf_group]),
        )[0]
        priority_sum += priority[common_item_type]
    return priority_sum
