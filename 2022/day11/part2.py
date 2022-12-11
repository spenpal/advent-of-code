# IMPORTS
import math

# GLOBALS
monkeys = {
    0: {
        "items": [84, 66, 62, 69, 88, 91, 91],
        "op": "*",
        "op_num": 11,
        "d_test": 2,
        "t_monkey": 4,
        "f_monkey": 7,
        "inspect_count": 0,
    },
    1: {
        "items": [98, 50, 76, 99],
        "op": "**",
        "op_num": 2,
        "d_test": 7,
        "t_monkey": 3,
        "f_monkey": 6,
        "inspect_count": 0,
    },
    2: {
        "items": [72, 56, 94],
        "op": "+",
        "op_num": 1,
        "d_test": 13,
        "t_monkey": 4,
        "f_monkey": 0,
        "inspect_count": 0,
    },
    3: {
        "items": [55, 88, 90, 77, 60, 67],
        "op": "+",
        "op_num": 2,
        "d_test": 3,
        "t_monkey": 6,
        "f_monkey": 5,
        "inspect_count": 0,
    },
    4: {
        "items": [69, 72, 63, 60, 72, 52, 63, 78],
        "op": "*",
        "op_num": 13,
        "d_test": 19,
        "t_monkey": 1,
        "f_monkey": 7,
        "inspect_count": 0,
    },
    5: {
        "items": [89, 73],
        "op": "+",
        "op_num": 5,
        "d_test": 17,
        "t_monkey": 2,
        "f_monkey": 0,
        "inspect_count": 0,
    },
    6: {
        "items": [78, 68, 98, 88, 66],
        "op": "+",
        "op_num": 6,
        "d_test": 11,
        "t_monkey": 2,
        "f_monkey": 5,
        "inspect_count": 0,
    },
    7: {
        "items": [70],
        "op": "+",
        "op_num": 7,
        "d_test": 5,
        "t_monkey": 1,
        "f_monkey": 3,
        "inspect_count": 0,
    },
}

LCM = math.lcm(*[monkeys[monkey_num]["d_test"] for monkey_num in monkeys])


# FUNCTIONS
# Simple calculator function
def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    elif op == "**":
        return num1**num2
    else:
        return "Invalid operator"


# MAIN
for _ in range(10000):
    for monkey_num in monkeys:
        for item in monkeys[monkey_num]["items"]:
            worry_level = calculate(
                item, monkeys[monkey_num]["op"], monkeys[monkey_num]["op_num"]
            )
            worry_level = worry_level % LCM

            if worry_level % monkeys[monkey_num]["d_test"] == 0:
                new_monkey_owner = monkeys[monkey_num]["t_monkey"]
            else:
                new_monkey_owner = monkeys[monkey_num]["f_monkey"]
            monkeys[new_monkey_owner]["items"].append(worry_level)

        monkeys[monkey_num]["inspect_count"] += len(monkeys[monkey_num]["items"])
        monkeys[monkey_num]["items"] = []

top_inspection_counts = list(
    sorted(
        [monkeys[monkey_num]["inspect_count"] for monkey_num in monkeys], reverse=True
    )
)
print(top_inspection_counts[0] * top_inspection_counts[1])
