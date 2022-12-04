import string

priority = {let: p+1 for p, let in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

with open("input.txt") as f:
    priority_sum = 0
    for line in f:
        rucksack = line.strip()
        compartments = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common_item_type = list(set(compartments[0]) & set(compartments[1]))[0]
        priority_sum += priority[common_item_type]

print(priority_sum)