import heapq

push, pop = heapq.heappush, heapq.heappop  # create aliases for heapq functions


def parse(data: str) -> dict[int, tuple]:
    data = data.splitlines()
    return {1: (data,), 2: (data,)}


def getSuccessors(cavern, state):
    length = len(cavern)
    row, col = state
    successors = []

    for nextRow, nextCol in [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]:
        if 0 <= nextRow < length and 0 <= nextCol < length:
            stepCost = cavern[nextRow][nextCol]
            successors.append((stepCost, (nextRow, nextCol)))

    return successors


def uniformCostSearch(cavern):
    length = len(cavern)
    start = (0, (0, 0))  # (gCost, state)

    fringe, visited = [], set()
    push(fringe, start)

    while fringe:
        node = pop(fringe)
        gCost, state = node

        if state in visited:
            continue
        visited.add(state)

        if state == (length - 1, length - 1):
            return gCost

        successors = getSuccessors(cavern, state)
        for succ_stepCost, succ_state in successors:
            succ_node = (gCost + succ_stepCost, succ_state)
            push(fringe, succ_node)

    return []


def part1(data):
    cavern = [[int(chiton) for chiton in row] for row in data]
    return uniformCostSearch(cavern)


def part2(data):
    length, newLength = len(data), len(data) * 5
    cavern = [[int(chiton) for chiton in row] for row in data]

    # expand remainder of first row
    for row in cavern:
        currRow = [int(chiton) for chiton in row]
        for _ in range(4):
            nextRow = [(chiton % 9) + 1 for chiton in currRow]
            row.extend(nextRow)
            currRow = nextRow

    # fill in rest of rows
    for row_idx in range(length, newLength):
        currRow = cavern[row_idx - length]
        nextRow = [(chiton % 9) + 1 for chiton in currRow]
        cavern.append(nextRow)

    return uniformCostSearch(cavern)
