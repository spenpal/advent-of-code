from functools import cache


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().split(" ")
    return {1: (data,), 2: (data,)}


@cache
def blink_stone(stone: str, blinks: int, max_blinks: int) -> int:
    if blinks == max_blinks:
        return 1

    next_stones = []
    if stone == "0":
        next_stones.append("1")
    elif len(stone) % 2 == 0:
        half = len(stone) // 2
        left_half, right_half = stone[:half], stone[half:].lstrip("0") or "0"
        next_stones.append(left_half)
        next_stones.append(right_half)
    else:
        next_stones.append(str(int(stone) * 2024))

    return sum(blink_stone(stone, blinks + 1, max_blinks) for stone in next_stones)


def part1(stones: list[str]) -> int:
    return sum(blink_stone(stone, 0, 25) for stone in stones)


def part2(stones: list[str]) -> int:
    return sum(blink_stone(stone, 0, 75) for stone in stones)
