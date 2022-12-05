stacks = [
    ['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
    ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
    ['V', 'C', 'R', 'S', 'Z'],
    ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
    ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
    ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
    ['G', 'C', 'V', 'B', 'P', 'Q'],
    ['Z', 'B', 'P', 'N'],
    ['W', 'P', 'J'],
]

import re

with open("input.txt") as f:
    for line in f:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        crates = int(match.group(1))
        from_stack, to_stack = int(match.group(2)) - 1, int(match.group(3)) - 1
        
        stacks[to_stack].extend(stacks[from_stack][-crates:])
        stacks[from_stack] = stacks[from_stack][:-crates]
        
print("".join([stack[-1] for stack in stacks]))