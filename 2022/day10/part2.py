# IMPORTS
import re

# GLOBALS
ADDX = re.compile(r"addx (-?\d+)")
NOOP = re.compile(r"noop")
X = 1
CRT = [""] * (40 * 6)


# MAIN
with open("input.txt") as f:
    cycle_num = 0

    for line in f:
        line = line.strip()
        flag = 0
        while flag < 2:
            cycle_num += 1
            flag += 1

            sprite_position = (X - 1, X, X + 1)
            CRT[cycle_num - 1] += (
                "#" if ((cycle_num - 1) % 40) in sprite_position else "."
            )

            if (match := ADDX.match(line)) and flag == 2:
                add_num = int(match[1])
                X += add_num
            elif NOOP.match(line):
                flag = 2  # End of Cycle

print("\n".join("".join(CRT[i : i + 40]) for i in range(0, len(CRT), 40)))
