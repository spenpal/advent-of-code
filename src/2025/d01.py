from src.utils import wrap_step

MIN_DIAL_NUMBER = 0
MAX_DIAL_NUMBER = 99
STARTING_DIAL_NUMBER = 50


def parse(data: str) -> dict[int, tuple]:
    rotations = data.replace("L", "-").replace("R", "")
    rotations = [int(num) for num in rotations.strip().splitlines()]
    return {1: (rotations,), 2: (rotations,)}


def part1(rotations: list[int]) -> int:
    times_at_zero = 0
    dial_position = STARTING_DIAL_NUMBER
    for rotation in rotations:
        dial_position, _ = wrap_step(
            val=dial_position,
            min_val=MIN_DIAL_NUMBER,
            max_val=MAX_DIAL_NUMBER,
            step=rotation,
        )
        times_at_zero += dial_position == 0
    return times_at_zero


def part2(rotations: list[int]) -> int:
    times_pointed_at_zero = 0
    dial_position = STARTING_DIAL_NUMBER
    for rotation in rotations:
        new_dial_position, wrap_count = wrap_step(
            val=dial_position,
            min_val=MIN_DIAL_NUMBER,
            max_val=MAX_DIAL_NUMBER,
            step=rotation,
        )
        if new_dial_position == 0 and rotation < 0:
            times_pointed_at_zero += abs(wrap_count) + 1
        elif (
            dial_position == 0 and rotation < 0 and new_dial_position > MIN_DIAL_NUMBER
        ):
            times_pointed_at_zero += abs(wrap_count) - 1
        else:
            times_pointed_at_zero += abs(wrap_count)
        dial_position = new_dial_position
    return times_pointed_at_zero
