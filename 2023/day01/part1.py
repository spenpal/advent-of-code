# IMPORTS
import re

# MAIN
with open("input.txt") as f:
    sum = 0
    for line in f:
        nums = re.findall(r"\d", line)
        sum += int(nums[0] + nums[-1])
    print(sum)
