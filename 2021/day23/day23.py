from pprint import pprint
from collections import deque

goalState = {
    'A': ((3,2), (3,3)),
    'B': ((5,2), (5,3)),
    'C': ((7,2), (7,3)),
    'D': ((9,2), (9,3))
}

cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

def manhattanDistance(s1, s2):
    return sum(abs(p2 - p1) for p1, p2 in zip(s1, s2))

def heuristic(state):
    h_val = 0
    
    for amphipod, spaces in state.items():
        goal_spaces = goalState[amphipod]
        
        goal_dists = [manhattanDistance(space, goal_space) for space in spaces for goal_space in goal_spaces]
        min_dist, max_dist = min(goal_dists), max(goal_dists)
        h_val += (min_dist + max_dist)
        
    return h_val

def getSuccessors(burrow, space):
    row, col = space
    successors = []
    
    for nextRow, nextCol in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if burrow[nextRow][nextCol] == '.':
            successors.append((nextRow, nextCol))
    
    return successors

def breadthFirstSearch(burrow, start, goal):
    start = (0, start) # (steps, start_space)
    
    fringe, visited = deque(), set()
    fringe.append(start)
    
    while fringe:
        steps, space = fringe.popleft()
        
        if space in visited: continue
        visited.add(space)
        
        if space == goal: return steps
        
        successors = getSuccessors(burrow, space)
        for succ_space in successors:
            succ = (steps + 1, succ_space)
            fringe.append(succ)
    
    return -1

def getState(burrow):
    state = {
        'A': (),
        'B': (),
        'C': (),
        'D': ()
    }
    
    for r_idx, row in enumerate(burrow):
        for c_idx, space in enumerate(row):
            if space in state:
                state[space] += ((r_idx, c_idx))
                
    return state

def nextLetterToMove(burrow):
    state = getState(burrow)

def part1(burrow):
    pass

def part2(burrow):
    pass

def main():
    with open("puzzle_input.txt") as f:
        burrow = f.read().splitlines()
        max_len = len(max(burrow, key=len))
        burrow = [list(row.replace(' ', '#').ljust(max_len, '#')) for row in burrow]
    
    print(f"Part 1 Answer: {part1(burrow)}")
    print(f"Part 2 Answer: {part2(burrow)}")

if __name__ == "__main__":
    main()