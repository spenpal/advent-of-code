def parse(data: str) -> dict[int, tuple]:
    data = data.strip()
    return {1: (data,), 2: (data,)}


def part1(data):
    window_length = 4
    i = 0
    while i <= len(data) - window_length:
        four_letters = data[i : i + window_length]
        if len(set(four_letters)) == window_length:
            break
        i += 1
    return i + window_length


def part2(data):
    window_length = 14
    i = 0
    while i <= len(data) - window_length:
        four_letters = data[i : i + window_length]
        if len(set(four_letters)) == window_length:
            break
        i += 1
    return i + window_length
