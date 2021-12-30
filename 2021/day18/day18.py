from math import floor, ceil
from copy import deepcopy

class Integer():
    def __init__(self, val = 0):
        self.val = int(val)
    def __iadd__(self, val):
        self.val += val
        return self
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

def magnitude(snum):
    if isinstance(snum, Integer): return snum.val
    return (3 * magnitude(snum[0])) + (2 * magnitude(snum[1]))

def flatten(container):
    for ele in container:
        if isinstance(ele, list): yield from flatten(ele)
        else: yield ele
        
def reduce(snum):
    
    def explode(snum, flat_snum, lvl):
        if lvl == 4:
            for idx, ele in enumerate(snum):
                if isinstance(ele, list):
                    left, right = ele
                    snum[idx] = Integer(0)
                    
                    next_left, next_right = flat_snum.index(left) - 1, flat_snum.index(right) + 1
                    if next_left >= 0: 
                        flat_snum[next_left] += left.val
                    if next_right < len(flat_snum): 
                        flat_snum[next_right] += right.val
                    
                    return True
        else:
            for ele in snum:
                if isinstance(ele, list): 
                    if explode(ele, flat_snum, lvl + 1): return True
                
        return False
        
    def split(snum, flat_snum, lvl):
        for idx, ele in enumerate(snum):
            if isinstance(ele, list):
                if split(ele, flat_snum, lvl + 1): return True
            elif ele.val > 9:
                snum[idx] = [Integer(floor(ele.val / 2)), Integer(ceil(ele.val / 2))]
                return True

    while True:
        flat_snum = list(flatten(snum))
        if explode(snum, flat_snum, 1): continue
        if split(snum, flat_snum, 1): continue
        break

def add(snum1, snum2):
    return [snum1, snum2]

def toInteger(container):
    for idx, ele in enumerate(container):
        if isinstance(ele, int): container[idx] = Integer(ele)
        else: toInteger(ele)
    return container

def part1(f):
    snum1, snum2 = toInteger(eval(f.readline().strip())), toInteger(eval(f.readline().strip()))
    result = add(snum1, snum2)
    reduce(result)
    
    for line in f:
        new_snum = toInteger(eval(line.strip()))
        result = add(result, new_snum)
        reduce(result)
    
    return magnitude(result)

def part2(snums):
    largest_magnitude = float('-inf')
    
    for snum1 in snums:
        for snum2 in snums:
            result = add(deepcopy(snum1), deepcopy(snum2))
            reduce(result)
            largest_magnitude = max(largest_magnitude, magnitude(result))
            
    return largest_magnitude
        
def main():
    f1 = open("puzzle_input.txt")
    with open("puzzle_input.txt") as f2:
        snums = f2.read().splitlines()
        snums = [toInteger(eval(snum)) for snum in snums]
    
    print(f"Part 1 Answer: {part1(f1)}")
    print(f"Part 2 Answer: {part2(snums)}")
    
if __name__ == "__main__":
    main()