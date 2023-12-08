# IMPORTS
from collections import Counter

# MAIN
copies = Counter()

with open("input") as f:
    for idx, line in enumerate(f, start=1):
        line = line.strip()
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums, my_nums = set(map(int, winning_nums.split())), set(
            map(int, my_nums.split())
        )
        same_nums = winning_nums & my_nums
        copies[idx] = copies.get(idx, 0) + 1
        for num in range(idx + 1, idx + len(same_nums) + 1):
            copies[num] = copies.get(num, 0) + copies[idx]
    print(sum(copies.values()))
