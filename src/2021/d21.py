from collections import Counter


def parse(data: str) -> dict[int, tuple]:
    data = data.splitlines()
    p1 = int(data[0].strip().split(": ")[-1])
    p2 = int(data[1].strip().split(": ")[-1])
    return {1: (p1, p2), 2: (p1, p2)}


def getState(s):
    s = s.copy()
    s["moves"] = sum(s["moves"])
    return tuple(s.items())


def next_pos(cur_pos):
    return ((cur_pos - 1) % 10) + 1


def part1(p1, p2):
    p1_score = p2_score = 0
    num_of_rolls = 0
    dd_rolls = [1, 2, 3]
    turn = 1

    while p1_score < 1000 and p2_score < 1000:
        move_sum = sum(dd_rolls)
        match turn:
            case 1:
                p1 = next_pos(p1 + move_sum)
                p1_score += p1
                turn = 2
            case 2:
                p2 = next_pos(p2 + move_sum)
                p2_score += p2
                turn = 1

        dd_rolls = [(((roll + 3) - 1) % 100) + 1 for roll in dd_rolls]
        num_of_rolls += 3

    return min(p1_score, p2_score) * num_of_rolls


def part2(p1, p2):
    def quantum(data, wins, mem):
        if not (data["p1_score"] < 21 and data["p2_score"] < 21):
            wins["p1"] += data["p1_score"] > data["p2_score"]
            wins["p2"] += data["p2_score"] > data["p1_score"]
            return

        state = getState(data)

        if len(data["moves"]) < 3:
            for move in range(1, 4):
                next_data = data.copy()
                next_data["moves"] += (move,)
                quantum(next_data, wins, mem)
        elif state in mem:
            wins.update(mem[state])
        else:
            next_data = data.copy()
            move_sum = sum(data["moves"])
            match data["turn"]:
                case 1:
                    next_data["p1"] = next_pos(next_data["p1"] + move_sum)
                    next_data["p1_score"] += next_data["p1"]
                    next_data["turn"] = 2
                case 2:
                    next_data["p2"] = next_pos(next_data["p2"] + move_sum)
                    next_data["p2_score"] += next_data["p2"]
                    next_data["turn"] = 1

            next_data["moves"] = ()
            prev_wins = wins.copy()
            quantum(next_data, wins, mem)
            new_wins = wins.copy()
            mem[state] = new_wins - prev_wins

    data = {"p1": p1, "p2": p2, "p1_score": 0, "p2_score": 0, "turn": 1, "moves": ()}
    wins = Counter({"p1": 0, "p2": 0})
    quantum(data, wins, {})
    return max(wins.values())
