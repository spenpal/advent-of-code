import re


def parse(data: str) -> dict[int, tuple]:
    data = "".join(line.strip() for line in data.splitlines())
    return {1: (data,), 2: (data,)}


def part1(memory: str) -> int:
    instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    return sum(int(x) * int(y) for x, y in instructions)


def part2(memory: str) -> int:
    memory_segments = (do.split("don't()")[0] for do in memory.split("do()"))
    return part1("".join(memory_segments))
