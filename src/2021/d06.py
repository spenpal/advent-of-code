from collections import Counter


def parse(data: str) -> dict[int, tuple]:
    fishes = data.strip().split(",")
    fishes = list(map(int, fishes))
    return {1: (fishes,), 2: (fishes,)}


def part1(fishes):
    for day in range(80):
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    return len(fishes)


def part2(fishes):
    timers = Counter(dict.fromkeys(range(10), 0))
    fishes = Counter(fishes)
    fishes.update(timers)

    for day in range(256):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}

    return sum(fishes.values())
