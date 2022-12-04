import string
from itertools import islice

priority = {let: p+1 for p, let in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

with open("input.txt") as f:
    priority_sum = 0
    while (elf_group := list(islice(f, 3))):
        common_item_type = list(set.intersection(*[set(rucksack.strip()) for rucksack in elf_group]))[0]
        priority_sum += priority[common_item_type]

print(priority_sum)