import re
from pprint import pprint
import time
from itertools import permutations

rotations = list(permutations(['x', 'y', 'z', '-x', '-y', '-z'], 3))
rotations = [rotation for rotation in rotations if len(set(axis[-1] for axis in rotation)) == 3]

def manhattan_distance(c1, c2):
    return sum(abs(x) for x in tuple(x2 - x1 for x1, x2 in zip(c1, c2)))
        
def convertCoords(loc, coords):
    return [tuple(x1 + x2 for x1, x2 in zip(loc, coord)) for coord in coords]

def slopes_and_distances(coords):
    
    def slope(c1, c2):
        return tuple(x2 - x1 for x1, x2 in zip(c1, c2))
        
    def distance(c1, c2):
        return sum((x2 - x1) ** 2 for x1, x2 in zip(c1, c2)) ** 0.5
    
    sads = {}
    for c1 in coords:
        for c2 in coords:
            if c1 == c2: continue
            s, d = slope(c1, c2), distance(c1, c2)
            sads[(s, d)] = (c1, c2)
        
    return sads

def find_overlap(s1_sads, s2_sads):
    overlap_beacons = {}
    
    for sad in s2_sads:
        if len(overlap_beacons) >= 12:
            s1c, s2c = list(overlap_beacons.items())[0]
            return tuple(x1 - x2 for x1, x2 in zip(s1c, s2c))
        if sad in s1_sads:
            overlap_beacons.update(zip(s1_sads[sad], s2_sads[sad]))
    
    return False

def rotate(coords):
    for rotation in rotations:
        yield [(eval(rotation[0]), eval(rotation[1]), eval(rotation[2])) for x, y, z in coords]

def assemble_map(beacons, scanner_locs, scanners):
    for s1 in range(len(scanners)):
        if s1 not in scanner_locs: continue
        s1_coords = scanners[s1]
        s1_sads = slopes_and_distances(s1_coords)
        
        for s2 in range(len(scanners)):
            if s2 in scanner_locs: continue
            
            for s2_coords in rotate(scanners[s2]):
                s2_sads = slopes_and_distances(s2_coords)
                if (s2_loc := find_overlap(s1_sads, s2_sads)):
                    new_coords = convertCoords(s2_loc, s2_coords)
                    if len(beacons & set(new_coords)) < 12: continue
                    
                    scanner_locs[s2], scanners[s2] = s2_loc, new_coords
                    beacons.update(scanners[s2])
                    break
                          
def part1(scanners):
    beacons = set(scanners[0])
    scanner_locs = {0: (0, 0)}
    
    while len(scanner_locs) < len(scanners):
        assemble_map(beacons, scanner_locs, scanners)
    
    return len(beacons), scanner_locs

def part2(scanner_locs):
    return max(manhattan_distance(scanner_locs[s1], scanner_locs[s2]) 
               for s1 in range(len(scanner_locs)) for s2 in range(s1, len(scanner_locs)))
    
def main():
    with open("puzzle_input.txt") as f:
        scanners = f.read().split('\n\n')
        scanner_data = {}
        
        for scanner in scanners:
            lines = scanner.splitlines()
            match = re.search(r'--- scanner (\d+) ---', lines[0])
            s_num = int(match[1])
            
            scanner_data[s_num] = []
            for line in lines[1:]:
                coords = eval(line)
                scanner_data[s_num].append(coords)
    
    num_of_beacons, scanner_locs = part1(scanner_data)
    print(f"Part 1 Answer: {num_of_beacons}")
    print(f"Part 2 Answer: {part2(scanner_locs)}")

if __name__ == "__main__":
    main()