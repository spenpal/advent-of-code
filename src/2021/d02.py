def parse(data) -> dict[int, tuple]:
    data = data.splitlines()
    return {1: (data,), 2: (data,)}


def part1(commands):
    position = {"horizontal": 0, "depth": 0}
    for command in commands:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            position["horizontal"] += units
        elif direction == "down":
            position["depth"] += units
        elif direction == "up":
            position["depth"] -= units
    return position["horizontal"] * position["depth"]


def part2(commands):
    position = {"horizontal": 0, "depth": 0, "aim": 0}
    for command in commands:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            position["horizontal"] += units
            position["depth"] += units * position["aim"]
        elif direction == "down":
            position["aim"] += units
        elif direction == "up":
            position["aim"] -= units
    return position["horizontal"] * position["depth"]
