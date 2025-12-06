from math import prod

from src.utils import all_same, transpose


def parse(data: str) -> dict[int, tuple]:
    # Part 1: Split tokens by whitespace (left-to-right reading)
    rows = [line.strip().split() for line in data.strip().splitlines()]

    # Part 2: Keep all characters including spaces (column-based reading)
    grid = [list(line) for line in data.splitlines()]

    return {1: (rows,), 2: (grid,)}


def part1(rows: list[list[str]]) -> int:
    problems: list[list[str]] = transpose(rows)
    total = 0

    for problem in problems:
        numbers: list[int] = map(int, problem[:-1])
        operation = problem[-1]  # Operation at the end of a problem
        match operation:
            case "*":
                total += prod(numbers)
            case "+":
                total += sum(numbers)

    return total


def part2(grid: list[list[str]]) -> int:
    # Each row is a digit sequence for one number
    rows: list[list[str]] = transpose(grid)
    num_rows = len(rows)

    total = row_idx = 0

    while row_idx < num_rows:
        operation = rows[row_idx][-1]  # Operation at end of the 1st number of a problem
        number_rows: list[list[str]] = []

        # Collect consecutive non-separator rows (each row = one number)
        while row_idx < num_rows and not all_same(rows[row_idx], " "):
            number_rows.append(rows[row_idx][:-1])  # Exclude operation column
            row_idx += 1

        numbers: list[int] = [int("".join(number_row)) for number_row in number_rows]

        match operation:
            case "*":
                total += prod(numbers)
            case "+":
                total += sum(numbers)

        row_idx += 1

    return total
