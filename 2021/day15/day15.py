import heapq

push, pop = heapq.heappush, heapq.heappop # create aliases for heapq functions

def getSuccessors(cavern, state):
    length = len(cavern)
    row, col = state
    successors = []
    
    for nextRow, nextCol in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= nextRow < length and 0 <= nextCol < length:
            stepCost = cavern[nextRow][nextCol]
            successors.append((stepCost, (nextRow, nextCol)))
    
    return successors
    
def uniformCostSearch(cavern):
    length = len(cavern)
    start = (0, (0, 0)) # (gCost, state)
    
    fringe, visited = [], set()
    push(fringe, start)
    
    while fringe:
        node = pop(fringe)
        gCost, state = node
        
        if state in visited: continue
        visited.add(state)
        
        if state == (length - 1, length - 1): return gCost
        
        successors = getSuccessors(cavern, state)
        for succ_stepCost, succ_state in successors:
            succ_node = (gCost + succ_stepCost, succ_state)
            push(fringe, succ_node)
    
    return []

def main():
    with open("puzzle_input.txt") as f:
        strCavern = f.read().splitlines()
        cavern1 = [[int(chiton) for chiton in row] for row in strCavern] # for part 1
        
        # For part 2
        length, newLength = len(strCavern), len(strCavern) * 5
        cavern2 = cavern1.copy()
        
        # expand remainder of first row
        for row in cavern2:
            currRow = [int(chiton) for chiton in row]
            for _ in range(4):
                nextRow = [(chiton % 9) + 1 for chiton in currRow]
                row.extend(nextRow)
                currRow = nextRow
        
        # fill in rest of rows
        for row_idx in range(length, newLength):
            currRow = cavern2[row_idx - length]
            nextRow = [(chiton % 9) + 1 for chiton in currRow]
            cavern2.append(nextRow)
                
    print(f"Part 1 Answer: {uniformCostSearch(cavern1)}")
    print(f"Part 2 Answer: {uniformCostSearch(cavern2)}")

if __name__ == "__main__":
    main()