points = {"Rock": 1, "Paper": 2, "Scissors": 3}

beater = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
beats = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}


def convert(letter):
    match letter:
        case "A" | "X":
            return "Rock"
        case "B" | "Y":
            return "Paper"
        case "C" | "Z":
            return "Scissors"


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    data = [line.split() for line in data]
    return {1: (data,), 2: (data,)}


def part1(data):
    def roundPts(opp_move, your_move):
        if beater[opp_move] == your_move:
            return points[your_move]
        if beater[your_move] == opp_move:
            return 6 + points[your_move]
        return 3 + points[your_move]

    total_pts = 0
    for opp_move, your_move in data:
        total_pts += roundPts(convert(opp_move), convert(your_move))
    return total_pts


def part2(data):
    def roundPts(opp_move, condition):
        if condition == "X":
            return points[beater[opp_move]]
        if condition == "Y":
            return 3 + points[opp_move]
        if condition == "Z":
            return 6 + points[beats[opp_move]]

    total_pts = 0
    for opp_move, condition in data:
        total_pts += roundPts(convert(opp_move), condition)
    return total_pts
