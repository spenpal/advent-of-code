import ast
from functools import cmp_to_key, partial
from itertools import islice


def parse(data: str) -> dict[int, tuple]:
    data = data.strip().splitlines()
    return {1: (data,), 2: (data,)}


def convert_pair(pair):
    left, right = pair[0].strip(), pair[1].strip()
    print(left, right)
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
        if left_v == right_v:
            truth = compare(left, right, i + 1)
        else:
            return left_v < right_v
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


def part1(data):
    data = iter(data)
    idx = 1
    right_order_idx = []
    while pair := list(islice(data, 2)):
        left, right = convert_pair(pair)
        right_order_idx += [idx] if compare(left, right, 0) else []
        idx += 1


def part2(data):
    packets = [packet for packet in data if packet]
    packets = [ast.literal_eval(packet) for packet in packets] + [[[2]], [[6]]]
    sorted_packets = sorted(packets, key=cmp_to_key(partial(compare, i=0)))
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
