from src.types import Grid, Pair

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

Path = list[tuple[Pair, Pair]]


def parse(data: str) -> dict[int, tuple]:
    data = [list(line.strip()) for line in data.strip().splitlines()]
    return {1: (data,), 2: (data,)}


def find_path(grid: Grid[str], pos: Pair, direction: Pair) -> Path | None:
    def valid_pos(x: int, y: int) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def rotate(direction: Pair) -> Pair:
        return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]

    path, visited = [], set()
    x, y = pos
    dx, dy = direction
    while True:
        step = (x, y), (dx, dy)
        if step in visited:
            return None

        path.append(step)
        visited.add(step)

        next_x, next_y = (x + dx), (y + dy)
        if not valid_pos(next_x, next_y):
            break
        if grid[next_x][next_y] == "#":
            dx, dy = rotate((dx, dy))
        else:
            x, y = next_x, next_y

    return path


def get_start_pos(grid: Grid[str]) -> Pair | None:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i, j)
    return None


def part1(grid: Grid[str]) -> int:
    pos = get_start_pos(grid)
    if not pos:
        return -1

    path = find_path(grid, pos, DIRECTIONS[0])
    if not path:
        return -1

    return len({pos for pos, _ in path})


def part2(grid: Grid[str]) -> int:
    pos = get_start_pos(grid)
    if not pos:
        return -1

    path = find_path(grid, pos, DIRECTIONS[0])
    if not path:
        return -1

    visited = set()
    total = 0
    for i in range(1, len(path)):
        obstacle_pos = path[i][0]
        pos, direction = path[i - 1]
        if obstacle_pos in visited or obstacle_pos == pos:
            continue

        grid[obstacle_pos[0]][obstacle_pos[1]] = "#"
        total += not find_path(grid, pos, direction)
        grid[obstacle_pos[0]][obstacle_pos[1]] = "."

        visited.add(obstacle_pos)

    return total
