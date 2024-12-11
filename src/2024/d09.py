def parse(data: str) -> dict[int, tuple]:
    disk_map = []
    for i, num in enumerate(data.strip()):
        if i % 2 == 0:
            disk_map.extend([i // 2] * int(num))
        else:
            disk_map.extend([None] * int(num))
    return {1: (disk_map,), 2: (disk_map,)}


def part1(disk_map: list[int | None]) -> int:
    left, right = 0, len(disk_map) - 1
    while left < right:
        if disk_map[left] is not None:
            left += 1
        elif disk_map[right] is None:
            right -= 1
        else:
            disk_map[left], disk_map[right] = disk_map[right], disk_map[left]
    return sum(i * num for i, num in enumerate(disk_map) if num is not None)


def part2(disk_map: list[int | None]) -> int:
    def find_free(end: int, count: int) -> int:
        free_space = 0
        for i in range(end):
            if disk_map[i] is not None:
                free_space = 0
            else:
                free_space += 1
            if free_space == count:
                return i - count + 1
        return -1

    count = 0
    for i in range(len(disk_map) - 1, 0, -1):
        count += 1
        if disk_map[i] != disk_map[i - 1]:
            if disk_map[i] is not None and (free_i := find_free(i, count)) >= 0:
                i_start, i_end = i, i + count
                free_i_start, free_i_end = free_i, free_i + count
                disk_map[free_i_start:free_i_end], disk_map[i_start:i_end] = (
                    disk_map[i_start:i_end],
                    disk_map[free_i_start:free_i_end],
                )
            count = 0

    return sum(i * num for i, num in enumerate(disk_map) if num is not None)
