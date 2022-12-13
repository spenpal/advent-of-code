# IMPORTS
import ast
from itertools import islice


# FUNCTIONS
def convert_pair(pair):
    left, right = pair[0].strip(), pair[1].strip()
    return ast.literal_eval(left), ast.literal_eval(right)


def compare(left, right, i):
    if len(left) <= i >= len(right):  # lists are same length and no difference found
        return None
    if i >= len(right):  # right list ran out of items
        return False
    if i >= len(left):  # left list ran out of items
        return True

    left_v, right_v = left[i], right[i]
    left_type, right_type = type(left_v), type(right_v)

    if left_type == int == right_type:  # both are ints
        if left_v > right_v:
            return False
        elif left_v < right_v:
            return True
        truth = compare(left, right, i + 1)
    elif left_type == list == right_type:  # both are lists
        truth = compare(left_v, right_v, 0)
    else:  # one is a list and the other is an int
        if left_type == int:
            left_v = [left_v]
        else:
            right_v = [right_v]
        truth = compare(left_v, right_v, 0)

    if truth == None:
        return compare(left, right, i + 1)
    return truth


# MAIN
with open("input.txt") as f:
    idx = 1
    right_order_idx = []
    while pair := list(islice(f, 2)):
        left, right = convert_pair(pair)
        right_order_idx += [idx] if compare(left, right, 0) else []
        idx += 1
        f.readline()

print(sum(right_order_idx))
