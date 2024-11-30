def parse(data: str) -> dict[int, tuple]:
    elfs_cals = []
    elf_total_cals = 0
    for line in data.splitlines():
        line = line.strip()
        if not line:
            elfs_cals.append(elf_total_cals)
            elf_total_cals = 0
        else:
            cals = int(line)
            elf_total_cals += cals
    return {1: (elfs_cals,), 2: (elfs_cals,)}


def part1(elfs_cals):
    return max(elfs_cals)


def part2(elfs_cals):
    return sum(sorted(elfs_cals, reverse=True)[:3])
