# IMPORTS
from collections import deque


# FUNCTIONS
def elevation(letter):
    if letter == "S":
        return ord("a")
    if letter == "E":
        return ord("z")
    return ord(letter)


def get_successors(height_map, state_x, state_y):
    curr_elevation = elevation(height_map[state_x][state_y])

    all_successors = [
        (state_x, state_y + 1),
        (state_x, state_y - 1),
        (state_x + 1, state_y),
        (state_x - 1, state_y),
    ]
    valid_successors = [
        succ
        for succ in all_successors
        if 0 <= succ[0] < len(height_map)
        and 0 <= succ[1] < len(height_map[0])
        and curr_elevation - elevation(height_map[succ[0]][succ[1]]) <= 1
    ]
    return valid_successors


def BFS(height_map, start_state):
    start = {"state": start_state, "cost": 0}

    fringe, visited = deque(), set()
    fringe.append(start)

    while fringe:
        node = fringe.popleft()  # Unpack next node from fringe

        if node.get("state") in visited:
            continue
        visited.add(node.get("state"))  # Add state to visited set

        state_x, state_y = node.get("state")
        if height_map[state_x][state_y] == "a":
            return node.get("cost")  # Return path cost if goal state is reached

        # Add successors to the fringe
        successors = get_successors(height_map, state_x, state_y)
        for succ_state in successors:
            succ_node = {"state": succ_state, "cost": node.get("cost") + 1}
            fringe.append(succ_node)

    return float("inf")  # Return infinity if no path is found


# MAIN
with open("input.txt") as f:
    height_map = f.read().splitlines()

    for ri, row in enumerate(height_map):
        for ci, ele in enumerate(row):
            if ele == "E":
                start_state = (ri, ci)
                break

print(BFS(height_map, start_state))
