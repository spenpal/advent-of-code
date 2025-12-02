from src.utils import factors, split_string


def parse(data: str) -> dict[int, tuple]:
    ranges: list[tuple[int, int]] = [
        tuple(map(int, range_str.split("-"))) for range_str in data.strip().split(",")
    ]
    return {1: (ranges,), 2: (ranges,)}


def part1(ranges: list[tuple[int, int]]) -> int:
    def is_repeated_twice(s: str) -> bool:
        return len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2 :]

    total = 0

    for start, end in ranges:
        for product_id in range(start, end + 1):
            if is_repeated_twice(str(product_id)):
                total += product_id

    return total


def part2(ranges: list[tuple[int, int]]) -> int:
    total = 0

    for start, end in ranges:
        for product_id in range(start, end + 1):
            id_str = str(product_id)

            # Get divisors that split the ID into 2+ equal parts
            divisors = factors(len(id_str))
            divisors.pop(0)  # Remove 1 (we need at least 2 repetitions)

            # Check if any split creates identical repeated segments
            if any(
                len(set(split_string(id_str, num_parts))) == 1 for num_parts in divisors
            ):
                total += product_id

    return total
