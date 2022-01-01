import re

def part1(yf_min):
    vy = (abs(yf_min) - 1)
    h_max = ((vy + 0.5) ** 2) / 2
    return round(h_max)

def part2(xf_min, xf_max, yf_min, yf_max):
    
    def hits_target(vx, vy):
        x = y = 0
        while True:
            # breaking conditions
            if x > xf_max: return False
            if vx == 0 and not xf_min <= x <= xf_max: return False
            if vx == 0 and y < yf_min: return False
            
            # target condition
            if xf_min <= x <= xf_max and yf_min <= y <= yf_max: return True
            
            x += vx
            y += vy
            
            if vx > 0: vx -= 1
            vy -= 1
    
    y_max = max(abs(yf_min), abs(yf_max))
    distinct_velocitys = 0
    
    for vx in range(xf_max + 1):
        for vy in range(-y_max, y_max + 1):
            distinct_velocitys += hits_target(vx, vy)
            
    return distinct_velocitys

def main():
    with open("puzzle_input.txt") as f:
        target_area = f.read().strip()
        x_match = re.search(r'x=(-?\d+)..(-?\d+)', target_area)
        y_match = re.search(r'y=(-?\d+)..(-?\d+)', target_area)
        xf_min, xf_max, yf_min, yf_max = int(x_match[1]), int(x_match[2]), int(y_match[1]), int(y_match[2])
    
    print(f"Part 1 Answer: {part1(yf_min)}")
    print(f"Part 2 Answer: {part2(xf_min, xf_max, yf_min, yf_max)}")

if __name__ == "__main__":
    main()