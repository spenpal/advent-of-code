points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

beater = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

beats = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock'
}


def convert(letter):
    match letter:
        case 'A' | 'X': 
            return 'Rock'
        case 'B' | 'Y':
            return 'Paper'
        case 'C' | 'Z':
            return 'Scissors'
        
        
def roundPts(opp_move, condition):
    if condition == 'X': return points[beater[opp_move]]
    if condition == 'Y': return 3 + points[opp_move]
    if condition == 'Z': return 6 + points[beats[opp_move]]


with open('input.txt', 'r') as f:
    total_pts = 0
    for line in f:
        data = line.strip().split()
        opp_move, condition = convert(data[0]), data[1] 
        total_pts += roundPts(opp_move, condition)
        
print(total_pts)