from pprint import pprint

def part1(cavern):
    solution = cavern.copy()
    length = len(solution)
    
    for col in range(1, length):
        solution[0][col] += solution[0][col - 1]
        
    for row in range(1, length):
        solution[row][0] += solution[row - 1][0]
        
    for row in range(1, length):
        for col in range(1, length):
            solution[row][col] += min(solution[row - 1][col], solution[row][col - 1])
    
    return solution[-1][-1] - solution[0][0]

def part2(cavern):
    pass

def main():
    with open("puzzle_input.txt") as f:
        cavern = [[int(risk) for risk in row] for row in f.read().splitlines()]

    print(f"Part 1 Answer: {part1(cavern)}")
    print(f"Part 2 Answer: {part2(cavern)}")

if __name__ == "__main__":
    main()