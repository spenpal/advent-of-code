def parse(data: str) -> dict[int, tuple]:
    data = data.strip().split(" ")
    return {1: (data,), 2: (data,)}


def change_stones(stones: list[str]) -> list[str]:
    next_stones = []
    for stone in stones:
        if stone == "0":
            next_stones.append("1")
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            left_half, right_half = stone[:half], stone[half:].lstrip("0") or "0"
            next_stones.append(left_half)
            next_stones.append(right_half)
        else:
            next_stones.append(str(int(stone) * 2024))
    return next_stones


def part1(stones: list[str]) -> int:
    for _ in range(25):
        stones = change_stones(stones)
    return len(stones)


def part2(stones: list[str]) -> int:
    for _ in range(75):
        stones = change_stones(stones)
    return len(stones)
