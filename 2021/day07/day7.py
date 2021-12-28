def explicit_sum(n):
    return (n * (n + 1)) // 2

def part1(crabs):
    crabs = [sum(abs(pos - crab) for crab in crabs) for pos in range(min(crabs), max(crabs) + 1)]
    return min(crabs)

def part2(crabs):
    crabs = [sum(explicit_sum(abs(pos - crab)) for crab in crabs) for pos in range(min(crabs), max(crabs) + 1)]
    return min(crabs)

def main():
    with open("puzzle_input.txt") as f:
        crabs = f.read().strip().split(',')
        crabs = list(map(int, crabs))
        
    print(f"Part 1 Answer: {part1(crabs)}")
    print(f"Part 2 Answer: {part2(crabs)}")

if __name__ == "__main__":
    main()