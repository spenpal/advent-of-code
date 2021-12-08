def part1(depths):
    increased_count = 0
    for idx in range(1, len(depths)):
        increased_count += depths[idx] > depths[idx - 1]
    return increased_count

def part2(depths):
    increased_window_count = 0
    for idx in range(3, len(depths)):
        first_window_sum = depths[idx - 1] + depths[idx - 2] + depths[idx - 3]
        second_window_sum = depths[idx] + depths[idx - 1] + depths[idx - 2]
        increased_window_count += second_window_sum > first_window_sum
    return increased_window_count

def main():
    with open('puzzle_input.txt') as f:
        depths = [int(line.strip()) for line in f]
        
    print(f'Part 1 Answer: {part1(depths)}')
    print(f'Part 2 Answer: {part2(depths)}')

if __name__ == '__main__':
    main()