def parse(data: str) -> dict[int, tuple]:
    lines = []
    for line in data.splitlines():
        line = line.strip()
        vents = line.split(" -> ")
        vent1 = tuple(map(int, vents[0].split(",")))
        vent2 = tuple(map(int, vents[1].split(",")))
        lines.append((vent1, vent2))
    return {1: (lines,), 2: (lines,)}


def sign(x):
    return 1 if x >= 0 else -1


def coveredPoints(x1, y1, x2, y2):
    line_points = []
    if x1 == x2:  # vertical line
        bit = -sign(y1 - y2)
        line_points = [(x1, y_point) for y_point in range(y1, y2 + bit, bit)]
    elif y1 == y2:  # horizontal line
        bit = -sign(x1 - x2)
        line_points = [(x_point, y1) for x_point in range(x1, x2 + bit, bit)]
    else:  # diagonal line
        x_bit = -sign(x1 - x2)
        y_bit = -sign(y1 - y2)
        x_points = [x_point for x_point in range(x1, x2 + x_bit, x_bit)]
        y_points = [y_point for y_point in range(y1, y2 + y_bit, y_bit)]
        line_points = zip(x_points, y_points, strict=False)
    return line_points


def part1(lines):
    point_overlap = {}
    for line in lines:
        (x1, y1), (x2, y2) = line
        if x1 == x2 or y1 == y2:
            line_points = coveredPoints(x1, y1, x2, y2)
            for line_point in line_points:
                point_overlap[line_point] = point_overlap.get(line_point, 0) + 1
    return sum(overlaps > 1 for overlaps in point_overlap.values())


def part2(lines):
    point_overlap = {}
    for line in lines:
        (x1, y1), (x2, y2) = line
        line_points = coveredPoints(x1, y1, x2, y2)
        for line_point in line_points:
            point_overlap[line_point] = point_overlap.get(line_point, 0) + 1
    return sum(overlaps > 1 for overlaps in point_overlap.values())
