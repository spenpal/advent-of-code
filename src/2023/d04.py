from collections import Counter


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    points = 0
    for line in data:
        line = line.strip()
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums, my_nums = (
            set(map(int, winning_nums.split())),
            set(map(int, my_nums.split())),
        )
        same_nums = winning_nums & my_nums
        points += 2 ** (len(same_nums) - 1) if same_nums else 0
    return points


def part2(data):
    copies = Counter()

    for idx, line in enumerate(data, start=1):
        line = line.strip()
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums, my_nums = (
            set(map(int, winning_nums.split())),
            set(
                map(int, my_nums.split()),
            ),
        )
        same_nums = winning_nums & my_nums
        copies[idx] = copies.get(idx, 0) + 1
        for num in range(idx + 1, idx + len(same_nums) + 1):
            copies[num] = copies.get(num, 0) + copies[idx]

    return sum(copies.values())
