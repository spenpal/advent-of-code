from src.utils import max_with_index


def parse(data: str) -> dict[int, tuple]:
    banks = [tuple(line.strip()) for line in data.strip().splitlines()]
    return {1: (banks,), 2: (banks,)}


def part1(banks: list[tuple[str, ...]]) -> int:
    total = 0

    for bank in banks:
        # Find first maximum digit
        first_max_idx, first_max = max_with_index(bank[:-1])

        # Find second maximum digit after first
        _, second_max = max_with_index(bank[first_max_idx + 1 :])

        total += int(f"{first_max}{second_max}")

    return total


def part2(banks: list[tuple[str]]) -> int:
    total = 0
    num_batteries = 12

    for bank in banks:
        joltage = ""
        bank_size = len(bank)
        start_idx = 0

        for remaining in range(num_batteries, 0, -1):
            # Find largest digit in valid window
            max_idx, max_digit = max_with_index(
                bank[start_idx : bank_size - remaining + 1],
            )
            joltage += max_digit
            start_idx += max_idx + 1

        total += int(joltage)

    return total
