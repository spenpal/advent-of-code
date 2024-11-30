import re

WORD_TO_NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    sum = 0
    for line in data:
        nums = re.findall(r"\d", line)
        sum += int(nums[0] + nums[-1])
    return sum


def part2(data):
    sum = 0
    for line in data:
        line = line.strip()
        pos = []

        # Add all numbers to a list of tuples (number, position)
        # First, add all number words and their positions to the list
        for key in WORD_TO_NUM:
            for match in re.finditer(key, line):
                pos.append((WORD_TO_NUM[key], match.span()[0]))

        # Next, add all numbers and their positions to the list
        for match in re.finditer(r"\d", line):
            pos.append((match.group(), match.span()[0]))

        # Sort the list by position
        pos.sort(key=lambda x: x[1])

        # Add the first and last numbers to the sum
        sum += int(pos[0][0] + pos[-1][0])

    return sum
