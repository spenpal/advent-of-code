# MAIN
with open("input") as f:
    points = 0
    for line in f:
        line = line.strip()
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums, my_nums = set(map(int, winning_nums.split())), set(
            map(int, my_nums.split())
        )
        same_nums = winning_nums & my_nums
        points += 2 ** (len(same_nums) - 1) if same_nums else 0
    print(points)
