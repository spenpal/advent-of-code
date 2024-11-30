def parse(data: str) -> dict[int, tuple]:
    coords, folds = set(), []

    for line in data.split("\n\n")[0].splitlines():
        x_coord, y_coord = line.split(",")
        coords.add((int(x_coord), int(y_coord)))

    for line in data.split("\n\n")[1].splitlines():
        fold_line = line.split()[-1]
        axis, loc = fold_line.split("=")
        folds.append((axis, int(loc)))

    return {1: (coords, folds), 2: (coords, folds)}


def part1(coords, folds):
    axis, loc = folds[0]
    temp_coords = coords.copy()

    for coord in coords:
        x, y = coord

        if axis == "x" and x > loc:
            x_flip = loc - (x - loc)
            temp_coords.remove(coord)
            temp_coords.add((x_flip, y))

        if axis == "y" and y > loc:
            y_flip = loc - (y - loc)
            temp_coords.remove(coord)
            temp_coords.add((x, y_flip))

    coords = temp_coords
    return len(coords)


def part2(coords, folds):
    for fold in folds:
        axis, loc = fold
        temp_coords = coords.copy()

        for coord in coords:
            x, y = coord

            if axis == "x" and x > loc:
                x_flip = loc - (x - loc)
                temp_coords.remove(coord)
                temp_coords.add((x_flip, y))

            if axis == "y" and y > loc:
                y_flip = loc - (y - loc)
                temp_coords.remove(coord)
                temp_coords.add((x, y_flip))

        coords = temp_coords

    # Used Desmos to graphically find the 'code'
    # Code was: PZEHRAER
    with open("final_coords.txt", "w") as f:
        for x, y in coords:
            f.write(f"({x}, {-y})\n")
