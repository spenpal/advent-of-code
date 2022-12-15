# IMPORTS
import re


# FUNCTIONS
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_coverage(sensor, cover_dist, y):
    y_range = (sensor[1] - cover_dist, sensor[1] + cover_dist)
    if y not in range(*y_range):
        return

    # returns one of the range ends, depending which is closer to y
    end = min(y_range, key=lambda e: abs(e - y))

    # using manhattan dist, it covers a "diamond shape" area, which follows the "2n - 1" formula
    x_cover_dist = 2 * (abs(end - y) + 1) - 1

    x_cover_range = (sensor[0] - (x_cover_dist // 2), sensor[0] + (x_cover_dist // 2))
    return x_cover_range


def remove_overlap(ranges, i):
    """
    Make sure ranges are sorted before calling this function
    """
    if i >= len(ranges) - 1:
        return

    range1, range2 = ranges[i], ranges[i + 1]
    overlap = (max(range1[0], range2[0]), min(range1[1], range2[1]))

    if overlap[0] <= overlap[1]:
        if overlap == range1:
            ranges.pop(i)
        elif overlap == range2:
            ranges.pop(i + 1)
        else:
            ranges.pop(i + 1)
            ranges.pop(i)
            ranges.insert(i, (range1[0], range2[1]))
        remove_overlap(ranges, i)
    elif overlap[0] - overlap[1] == 1:
        ranges.pop(i + 1)
        ranges.pop(i)
        ranges.insert(i, (range1[0], range2[1]))
        remove_overlap(ranges, i)
    else:
        remove_overlap(ranges, i + 1)


# MAIN
beacons = set()
sensor_cover = {}
max_bound = 4_000_000

with open("input.txt") as f:
    for line in f:
        coords = re.findall(r"-?\d+", line)
        coords = list(map(int, coords))
        sensor, beacon = tuple(coords[:2]), tuple(coords[2:])

        beacons.add(beacon)
        sensor_cover[sensor] = manhattan_distance(sensor, beacon)


for yi in range(max_bound + 1):
    y = yi
    x_cover_ranges = []

    for sensor, cover_dist in sensor_cover.items():
        if x_cover_range := find_coverage(sensor, cover_dist, y):
            x_cover_ranges.append(x_cover_range)

    # bound ranges
    for i, x_cover_range in enumerate(x_cover_ranges):
        start, end = x_cover_range
        new_start = 0 if start < 0 else start
        new_end = max_bound if end > max_bound else end
        x_cover_ranges[i] = (new_start, new_end)

    x_cover_ranges.sort()
    remove_overlap(x_cover_ranges, 0)

    if x_cover_ranges != [(0, max_bound)]:
        break

x_coord = x_cover_ranges[0][1] + 1
y_coord = y
print(f"Tuning Frequency: {(x_coord * 4_000_000) + y_coord}")

# overall running time of Part 2 is about a minute or so
