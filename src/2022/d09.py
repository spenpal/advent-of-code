def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def part1(data):
    def gap(head, tail):
        return abs(tail[0] - head[0]) >= 2 or abs(tail[1] - head[1]) >= 2

    def move(direction, distance, head, tail, tail_positions):
        for _ in range(distance):
            match direction:
                case "U":
                    head[1] += 1
                    if gap(head, tail):
                        tail[0], tail[1] = head[0], head[1] - 1
                case "D":
                    head[1] -= 1
                    if gap(head, tail):
                        tail[0], tail[1] = head[0], head[1] + 1
                case "L":
                    head[0] -= 1
                    if gap(head, tail):
                        tail[0], tail[1] = head[0] + 1, head[1]
                case "R":
                    head[0] += 1
                    if gap(head, tail):
                        tail[0], tail[1] = head[0] - 1, head[1]

            tail_positions.add(tuple(tail))

    head = [0, 0]
    tail = [0, 0]
    tail_positions = set()

    for line in data:
        line = line.strip().split()
        direction, distance = line[0], int(line[1])
        move(direction, distance, head, tail, tail_positions)

    return len(tail_positions)


def part2(data):
    def gap(knot1, knot2):
        return abs(knot2[0] - knot1[0]) >= 2 or abs(knot2[1] - knot1[1]) >= 2

    def update_other_knots(knots):
        for i in range(1, len(knots)):
            if not gap(knots[i - 1], knots[i]):
                break

            x_diff, y_diff = (
                (knots[i][0] - knots[i - 1][0]),
                (knots[i][1] - knots[i - 1][1]),
            )
            match (x_diff, y_diff):
                case (-2, 2):  # up-left
                    knots[i][0], knots[i][1] = knots[i - 1][0] - 1, knots[i - 1][1] + 1
                case (2, 2):  # up-right
                    knots[i][0], knots[i][1] = knots[i - 1][0] + 1, knots[i - 1][1] + 1
                case (-2, -2):  # down-left
                    knots[i][0], knots[i][1] = knots[i - 1][0] - 1, knots[i - 1][1] - 1
                case (2, -2):  # down-right
                    knots[i][0], knots[i][1] = knots[i - 1][0] + 1, knots[i - 1][1] - 1
                case (_, 2):  # up
                    knots[i][0], knots[i][1] = knots[i - 1][0], knots[i - 1][1] + 1
                case (_, -2):  # down
                    knots[i][0], knots[i][1] = knots[i - 1][0], knots[i - 1][1] - 1
                case (-2, _):  # left
                    knots[i][0], knots[i][1] = knots[i - 1][0] - 1, knots[i - 1][1]
                case (2, _):  # right
                    knots[i][0], knots[i][1] = knots[i - 1][0] + 1, knots[i - 1][1]

    def move(direction, distance, knots, tail_positions):
        head = knots[0]
        tail = knots[-1]

        for _ in range(distance):
            match direction:
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1

            update_other_knots(knots)
            tail_positions.add(tuple(tail))

    knots = [[0, 0] for _ in range(10)]
    tail_positions = set()

    for line in data:
        line = line.strip().split()
        direction, distance = line[0], int(line[1])
        move(direction, distance, knots, tail_positions)

    return len(tail_positions)
