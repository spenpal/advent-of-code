with open("input.txt") as f:
    complete_overlap_pairs = 0
    for line in f:
        elf1, elf2 = line.strip().split(',')
        elf1 = tuple(map(int, elf1.split('-')))
        elf2 = tuple(map(int, elf2.split('-')))
        
        overlap = (max(elf1[0], elf2[0]), min(elf1[1], elf2[1]))
        complete_overlap_pairs += (overlap == elf1 or overlap == elf2)
        
print(complete_overlap_pairs)