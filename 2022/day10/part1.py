# IMPORTS
import re

# GLOBALS
ADDX = re.compile(r"addx (-?\d+)")
NOOP = re.compile(r"noop")
X = 1


# MAIN
with open("input.txt") as f:
    signal_strengths = []
    cycle_num = 0

    for line in f:
        line = line.strip()
        flag = 0
        while flag < 2:
            cycle_num += 1
            flag += 1
            if cycle_num in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(cycle_num * X)
            if (match := ADDX.match(line)) and flag == 2:
                add_num = int(match[1])
                X += add_num
            elif NOOP.match(line):
                flag = 2  # End of Cycle

print(sum(signal_strengths))
