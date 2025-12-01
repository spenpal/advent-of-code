from collections import deque


def parse(data: str) -> dict[int, tuple]:
    data = [line.strip().split(": ") for line in data.strip().splitlines()]
    data = [(tuple(map(int, nums.split())), int(target)) for target, nums in data]
    return {1: (data,), 2: (data,)}


def part1(equations: list[tuple[tuple[int, ...], int]]) -> int:
    total = 0

    for nums, target in equations:
        queue = deque([(nums[0], nums[1:])])
        while queue:
            res, remainder_nums = queue.popleft()
            if not remainder_nums:
                if res == target:
                    total += target
                    break
                continue

            next_num = remainder_nums[0]
            add, mul = res + next_num, res * next_num

            if add <= target:
                queue.append((add, remainder_nums[1:]))
            if mul <= target:
                queue.append((mul, remainder_nums[1:]))

    return total


def part2(equations: list[tuple[tuple[int, ...], int]]) -> int:
    total = 0

    for nums, target in equations:
        queue = deque([(nums[0], nums[1:])])
        while queue:
            res, remainder_nums = queue.popleft()
            if not remainder_nums:
                if res == target:
                    total += target
                    break
                continue

            next_num = remainder_nums[0]
            add, mul, concat = (res + next_num, res * next_num, int(str(res) + str(next_num)))

            if add <= target:
                queue.append((add, remainder_nums[1:]))
            if mul <= target:
                queue.append((mul, remainder_nums[1:]))
            if concat <= target:
                queue.append((concat, remainder_nums[1:]))

    return total
