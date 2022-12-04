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


def convert(letter):
    match letter:
        case 'A' | 'X': 
            return 'Rock'
        case 'B' | 'Y':
            return 'Paper'
        case 'C' | 'Z':
            return 'Scissors'
        
        
def roundPts(opp_move, your_move):
    if beater[opp_move] == your_move: return points[your_move]
    if beater[your_move] == opp_move: return 6 + points[your_move]
    return 3 + points[your_move]


with open('input.txt', 'r') as f:
    total_pts = 0
    for line in f:
        opp_move, your_move = [convert(letter) for letter in line.strip().split()]
        total_pts += roundPts(opp_move, your_move)
        
print(total_pts)