def sign(x): 
  return 1 if x >= 0 else -1

def coveredPoints(x1, y1, x2, y2):
    line_points = []
    if x1 == x2: # vertical line
        bit = -sign(y1 - y2)
        line_points = [(x1, y_point) for y_point in range(y1, y2 + bit, bit)]
    elif y1 == y2: # horizontal line
        bit = -sign(x1 - x2)
        line_points = [(x_point, y1) for x_point in range(x1, x2 + bit, bit)]
    else: # diagonal line
        x_bit = -sign(x1 - x2)
        y_bit = -sign(y1 - y2)
        x_points = [x_point for x_point in range(x1, x2 + x_bit, x_bit)]
        y_points = [y_point for y_point in range(y1, y2 + y_bit, y_bit)]
        line_points = zip(x_points, y_points)
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

def main():
    with open("puzzle_input.txt") as f:
        lines = []
        for line in f:
            line = line.strip()
            vents = line.split(' -> ')
            vent1 = tuple(map(int, vents[0].split(',')))
            vent2 = tuple(map(int, vents[1].split(',')))
            lines.append((vent1, vent2))
    
    print(f"Part 1 Answer: {part1(lines)}")
    print(f"Part 2 Answer: {part2(lines)}")

if __name__ == "__main__":
    main()