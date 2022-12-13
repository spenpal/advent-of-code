# IMPORTS
import ast
from functools import cmp_to_key, partial


# FUNCTIONS
def convert_pair(pair):
    left, right = pair[0].strip(), pair[1].strip()
    return ast.literal_eval(left), ast.literal_eval(right)


def compare(left, right, i):
    if len(left) <= i >= len(right):  # lists are same length and no difference found
        return 0
    if i >= len(right):  # right list ran out of items
        return 1
    if i >= len(left):  # left list ran out of items
        return -1

    left_v, right_v = left[i], right[i]
    left_type, right_type = type(left_v), type(right_v)

    if left_type == int == right_type:  # both are ints
        if left_v == right_v:
            truth = compare(left, right, i + 1)
        else:
            return -1 if left_v < right_v else 1
    elif left_type == list == right_type:  # both are lists
        truth = compare(left_v, right_v, 0)
    else:  # one is a list and the other is an int
        if left_type == int:
            left_v = [left_v]
        else:
            right_v = [right_v]
        truth = compare(left_v, right_v, 0)

    if truth == 0:
        return compare(left, right, i + 1)
    return truth


# MAIN
with open("input.txt") as f:
    packets = [packet for packet in f.read().splitlines() if packet]
    packets = [ast.literal_eval(packet) for packet in packets] + [[[2]], [[6]]]
    sorted_packets = sorted(packets, key=cmp_to_key(partial(compare, i=0)))
    decoder_key = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
    print(decoder_key)
