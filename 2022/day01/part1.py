with open('input.txt') as f:
    elfs_cals = []
    elf_total_cals = 0
    for line in f:
        line = line.strip()
        if not line:
            elfs_cals.append(elf_total_cals)
            elf_total_cals = 0
        else:
            cals = int(line)
            elf_total_cals += cals
            
print(max(elfs_cals))
        