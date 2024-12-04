import re


def parse(data: str) -> dict[int, tuple]:
    data = data.strip()
    return {1: (data,), 2: (data,)}


def part1(memory: str) -> int:
    instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    return sum(int(x) * int(y) for x, y in instructions)


def part2(memory: str) -> int:
    memory_segments = re.split(r"(don't\(\)|do\(\))", memory)
    return part1(memory_segments[0]) + sum(
        part1(segment)
        for condition, segment in zip(
            memory_segments[1::2], memory_segments[2::2], strict=False
        )
        if condition == "do()"
    )
