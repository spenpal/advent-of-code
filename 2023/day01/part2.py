# IMPORTS
import re

# CONSTANTS
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


# MAIN
with open("input.txt") as f:
    sum = 0
    for line in f:
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

    print(sum)
