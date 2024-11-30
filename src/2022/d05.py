import re

stacks = [
    ["N", "B", "D", "T", "V", "G", "Z", "J"],
    ["S", "R", "M", "D", "W", "P", "F"],
    ["V", "C", "R", "S", "Z"],
    ["R", "T", "J", "Z", "P", "H", "G"],
    ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    ["N", "V", "P", "W", "G", "S", "F", "M"],
    ["G", "C", "V", "B", "P", "Q"],
    ["Z", "B", "P", "N"],
    ["W", "P", "J"],
]


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().split("\n\n")
    return {1: (data[1],), 2: (data[1],)}


def part1(data):
    for line in data:
        # match the line and group the numbers: "move 2 from 4 to 6"
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        crates = int(match.group(1))
        from_stack, to_stack = int(match.group(2)) - 1, int(match.group(3)) - 1

        # move the crates from the "from_stack" to the "to_stack" in the stacks array
        stacks[to_stack].extend(stacks[from_stack][: -(crates + 1) : -1])
        stacks[from_stack] = stacks[from_stack][:-crates]
    return "".join([stack[-1] for stack in stacks])


def part2(data):
    for line in data:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        crates = int(match.group(1))
        from_stack, to_stack = int(match.group(2)) - 1, int(match.group(3)) - 1

        stacks[to_stack].extend(stacks[from_stack][-crates:])
        stacks[from_stack] = stacks[from_stack][:-crates]
    return "".join([stack[-1] for stack in stacks])
