import re
import math

def oppState(state):
    return 'off' if state == 'on' else 'on'

def intersection(c1, c2):
    
    def plane_intersection(r1, r2):
        i = (max(r1[0], r2[0]), min(r1[-1], r2[-1]))
        return i if i[0] <= i[1] else ()
    
    inter = tuple(plane_intersection(r1, r2) for r1, r2 in zip(c1, c2))
    return inter if all(r for r in inter) else None

def total_cubes(core):
    return math.prod(r[1] - r[0] + 1 for r in core)

def part1(steps):
    reactor = {}
    
    for state, coords in steps:
        (x_min, x_max), (y_min, y_max), (z_min, z_max) = coords
        if not all(-50 <= i <= 50 for i in [x_min, x_max, y_min, y_max, z_min, z_max]): continue
        
        init = {(x, y, z): state for x in range(x_min, x_max + 1) 
                for y in range(y_min, y_max + 1) 
                for z in range(z_min, z_max + 1)}
        reactor.update(init)
        
    return sum(state == 'on' for state in reactor.values())

def part2(steps):
    """
    Read Reddit solution on Set Theory to do this one
    """
    reactor = []
    
    for cuboid_state, cuboid in steps:
        new_cores = [(cuboid_state, cuboid)] if cuboid_state == 'on' else []
        
        for core_state, core in reactor:
            if (inter := intersection(cuboid, core)):
                new_cores.append((oppState(core_state), inter))
                
        reactor.extend(new_cores)
        
    return sum((1 if state == 'on' else -1) * total_cubes(core) for state, core in reactor)
            
def main():
    with open("puzzle_input.txt") as f:
        steps = []
        for line in f:
            state, coords = line.split()
            match = re.search(r'x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', coords)
            x_min, x_max = int(match[1]), int(match[2])
            y_min, y_max = int(match[3]), int(match[4])
            z_min, z_max = int(match[5]), int(match[6])
            coords = ((x_min, x_max), (y_min, y_max), (z_min, z_max))
            steps.append((state, coords))
        
    print(f"Part 1 Answer: {part1(steps)}")
    print(f"Part 2 Answer: {part2(steps)}")

if __name__ == "__main__":
    main()