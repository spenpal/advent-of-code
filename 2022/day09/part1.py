# FUNCTIONS
def gap(head, tail):
    return abs(tail[0] - head[0]) >= 2 or abs(tail[1] - head[1]) >= 2


def move(direction, distance, head, tail, tail_positions):
    for _ in range(distance):
        match direction:
            case 'U':
                head[1] += 1
                if gap(head, tail):
                    tail[0], tail[1] = head[0], head[1] - 1
            case 'D':
                head[1] -= 1
                if gap(head, tail):
                    tail[0], tail[1] = head[0], head[1] + 1
            case 'L':
                head[0] -= 1
                if gap(head, tail):
                    tail[0], tail[1] = head[0] + 1, head[1]
            case 'R':
                head[0] += 1
                if gap(head, tail):
                    tail[0], tail[1] = head[0] - 1, head[1]
        
        tail_positions.add(tuple(tail))
    
    
# MAIN
with open("input.txt") as f:
    head = [0, 0]
    tail = [0, 0]
    tail_positions = set()
    
    for line in f:
        line = line.strip().split()
        direction, distance = line[0], int(line[1])
        move(direction, distance, head, tail, tail_positions)
        
print(len(tail_positions))