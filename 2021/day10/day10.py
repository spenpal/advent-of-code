openList, closeList = ['(', '[', '{', '<'], [')', ']', '}', '>']

def part1(chunks):
    points = {
        ')': 3, 
        ']': 57, 
        '}': 1197, 
        '>': 25137
    }
    
    chunkMap = dict(zip(closeList, openList))
    corruptChars = []
    
    for chunk in chunks:
        stack = []
        for char in chunk:
            if char in openList: stack.append(char)
            elif char in closeList:
                if chunkMap[char] == stack[-1]: stack.pop()
                else: corruptChars.append(char); break
    
    return sum(points[corruptChar] for corruptChar in corruptChars)
            
def part2(chunks):
    def chunkScore(chunk):
        points = {
            ')': 1, 
            ']': 2, 
            '}': 3, 
            '>': 4
        }
        return sum((5 ** idx) * points[char] for idx, char in enumerate(chunk))
    
    chunkMap = dict(zip(closeList, openList))
    reverseChunkMap = dict(zip(openList, closeList))
    incompleteChunks = []
    
    # Remove corrupted lines
    for chunk in chunks:
        stack = []
        incompleteChunks.append(chunk)
        for char in chunk:
            if char in openList: stack.append(char)
            elif char in closeList:
                if len(stack) and chunkMap[char] == stack[-1]: stack.pop()
                else: incompleteChunks.pop(); break
    
    # Get scores of all completed chunks
    chunkScores = []            
    for iChunk in incompleteChunks:
        stack = []
        for char in iChunk:
            if char in openList: stack.append(char)
            elif char in closeList:
                if len(stack) and chunkMap[char] == stack[-1]: stack.pop()
        completeChunk = [reverseChunkMap[char] for char in stack]
        chunkScores.append(chunkScore(completeChunk))
        
    return list(sorted(chunkScores))[len(chunkScores) // 2]
    
def main():
    with open("puzzle_input.txt") as f:
        chunks = f.read().splitlines()
        
    print(f"Part 1 Answer: {part1(chunks)}")
    print(f"Part 2 Answer: {part2(chunks)}")

if __name__ == "__main__":
    main()