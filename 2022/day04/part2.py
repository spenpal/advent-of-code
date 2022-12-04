with open("input.txt") as f:
    overlap_pairs = 0
    for line in f:
        elf1, elf2 = line.strip().split(',')
        elf1 = tuple(map(int, elf1.split('-')))
        elf2 = tuple(map(int, elf2.split('-')))
        
        overlap = (max(elf1[0], elf2[0]), min(elf1[1], elf2[1]))
        overlap_pairs += overlap[0] <= overlap[1]
        
print(overlap_pairs)