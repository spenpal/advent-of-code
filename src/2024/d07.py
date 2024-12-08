from itertools import product

from src.utils import merge


def parse(data: str) -> dict[int, tuple]:
    data = [line.strip().split(": ") for line in data.strip().splitlines()]
    data = [(tuple(numbers.split()), target) for target, numbers in data]
    return {1: (data,), 2: (data,)}


def calculate(numbers: tuple[str, ...], ops: tuple[str, ...], target: int) -> int:
    expr = merge(numbers, ops)
    stack = expr[::-1]

    while len(stack) > 1:
        left, op, right = stack.pop(), stack.pop(), stack.pop()

        match op:
            case "+":
                result = int(left) + int(right)
            case "*":
                result = int(left) * int(right)
            case "||":
                result = int(left + right)
            case _:
                msg = f"Unsupported operator: {op}"
                raise ValueError(msg)

        if result > target:
            return -1

        stack.append(str(result))

    return int(stack.pop())


def part1(equations: list[tuple[tuple[str, ...], str]]) -> int:
    total = 0
    for numbers, target in equations:
        target = int(target)
        op_perms = product(["+", "*"], repeat=len(numbers) - 1)
        if any(calculate(numbers, ops, target) == target for ops in op_perms):
            total += target
    return total


def part2(equations: list[tuple[tuple[str, ...], str]]) -> int:
    total = 0
    for numbers, target in equations:
        target = int(target)
        op_perms = product(["+", "*", "||"], repeat=len(numbers) - 1)
        if any(calculate(numbers, ops, target) == target for ops in op_perms):
            total += target
    return total
