import math


def parse(data: str) -> dict[int, tuple]:
    data = [list(map(int, list(row))) for row in data.splitlines()]
    return {1: (data,), 2: (data,)}


def checkLowPoint(hmap, row, col):
    point = hmap[row][col]
    row_size, col_size = len(hmap), len(hmap[0])

    upPoint = hmap[row - 1][col] if row - 1 >= 0 else 10
    leftPoint = hmap[row][col - 1] if col - 1 >= 0 else 10
    rightPoint = hmap[row][col + 1] if col + 1 < col_size else 10
    downPoint = hmap[row + 1][col] if row + 1 < row_size else 10

    return all(
        point < adjPoint for adjPoint in [upPoint, leftPoint, rightPoint, downPoint]
    )


def part1(hmap):
    low_points = []
    row_size, col_size = len(hmap), len(hmap[0])

    for row in range(row_size):
        for col in range(col_size):
            if checkLowPoint(hmap, row, col):
                low_points.append(hmap[row][col])

    return sum(low_point + 1 for low_point in low_points)


def part2(hmap):
    def findBasinSize(hmap, row, col, visited):
        if (
            not 0 <= row < len(hmap)
            or not 0 <= col < len(hmap[0])
            or (row, col) in visited
            or hmap[row][col] == 9
        ):
            return 0

        visited.add((row, col))
        return (
            findBasinSize(hmap, row - 1, col, visited)
            + findBasinSize(hmap, row + 1, col, visited)
            + findBasinSize(hmap, row, col - 1, visited)
            + findBasinSize(hmap, row, col + 1, visited)
            + 1
        )

    # Find low points
    low_points = []
    row_size, col_size = len(hmap), len(hmap[0])
    for row in range(row_size):
        for col in range(col_size):
            if checkLowPoint(hmap, row, col):
                low_points.append((row, col))

    # Find basin sizes
    top_three_basins = sorted(
        [findBasinSize(hmap, row, col, set()) for row, col in low_points],
        reverse=True,
    )[:3]
    return math.prod(top_three_basins)
