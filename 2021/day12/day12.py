from collections import Counter

def part1(cave_map):
    def distinct_paths(cave_map, path, paths):
        loc, visited = path[-1], path[:-1]
        if loc.islower() and loc in visited: return
        if loc == 'end': paths.append(path); return
        
        for next_loc in cave_map.get(loc):
            distinct_paths(cave_map, path.copy() + [next_loc], paths)
            
    paths = []
    distinct_paths(cave_map, ['start'], paths)
    return len(paths)

def part2(cave_map):
    def distinct_paths(cave_map, path, paths):
        loc, visited = path[-1], Counter(cave for cave in path[:-1] if cave.islower())
        if loc == 'start' and len(path) > 1: return
        if loc.islower() and (loc in visited) and (2 in list(visited.values())): return
        if loc == 'end': paths.append(','.join(path)); return
        
        for next_loc in cave_map.get(loc):
            distinct_paths(cave_map, path.copy() + [next_loc], paths)
            
    paths = []
    distinct_paths(cave_map, ['start'], paths)
    return len(paths)

def main():
    with open("puzzle_input.txt") as f:
        cave_map = {}
        for line in f:
            start, end = line.strip().split('-')
            cave_map[start] = cave_map.get(start, []) + [end]
            cave_map[end] = cave_map.get(end, []) + [start]
    
    print(f"Part 1 Answer: {part1(cave_map)}")
    print(f"Part 2 Answer: {part2(cave_map)}")

if __name__ == "__main__":
    main()