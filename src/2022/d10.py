import re

ADDX = re.compile(r"addx (-?\d+)")
NOOP = re.compile(r"noop")


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    x = 1
    signal_strengths = []
    cycle_num = 0

    for line in data:
        line = line.strip()
        flag = 0
        while flag < 2:
            cycle_num += 1
            flag += 1
            if cycle_num in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(cycle_num * x)
            if (match := ADDX.match(line)) and flag == 2:
                add_num = int(match[1])
                x += add_num
            elif NOOP.match(line):
                flag = 2  # End of Cycle

    return sum(signal_strengths)


def part2(data):
    x = 1
    crt = [""] * (40 * 6)
    cycle_num = 0

    for line in data:
        line = line.strip()
        flag = 0
        while flag < 2:
            cycle_num += 1
            flag += 1

            sprite_position = (x - 1, x, x + 1)
            crt[cycle_num - 1] += (
                "#" if ((cycle_num - 1) % 40) in sprite_position else "."
            )

            if (match := ADDX.match(line)) and flag == 2:
                add_num = int(match[1])
                x += add_num
            elif NOOP.match(line):
                flag = 2  # End of Cycle

    return "\n".join("".join(crt[i : i + 40]) for i in range(0, len(crt), 40))
