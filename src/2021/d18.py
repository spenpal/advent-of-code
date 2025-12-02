from copy import deepcopy
from math import ceil, floor


class Integer:
    def __init__(self, val=0):
        self.val = int(val)

    def __iadd__(self, val):
        self.val += val
        return self

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def toInteger(container):
    for idx, ele in enumerate(container):
        if isinstance(ele, int):
            container[idx] = Integer(ele)
        else:
            toInteger(ele)
    return container


def parse(data: str) -> dict[int, tuple]:
    data = data.splitlines()
    snums = [toInteger(eval(snum)) for snum in data]
    return {1: (data,), 2: (snums,)}


def magnitude(snum):
    if isinstance(snum, Integer):
        return snum.val
    return 3 * magnitude(snum[0]) + 2 * magnitude(snum[1])


def flatten(container):
    for ele in container:
        if isinstance(ele, list):
            yield from flatten(ele)
        else:
            yield ele


def reduce(snum):
    def explode(snum, flat_snum, lvl):
        if lvl == 4:
            for idx, ele in enumerate(snum):
                if isinstance(ele, list):
                    left, right = ele
                    snum[idx] = Integer(0)

                    next_left, next_right = (
                        flat_snum.index(left) - 1,
                        flat_snum.index(right) + 1,
                    )
                    if next_left >= 0:
                        flat_snum[next_left] += left.val
                    if next_right < len(flat_snum):
                        flat_snum[next_right] += right.val

                    return True
        else:
            for ele in snum:
                if isinstance(ele, list):
                    if explode(ele, flat_snum, lvl + 1):
                        return True

        return False

    def split(snum, flat_snum, lvl):
        for idx, ele in enumerate(snum):
            if isinstance(ele, list):
                if split(ele, flat_snum, lvl + 1):
                    return True
            elif ele.val > 9:
                snum[idx] = [Integer(floor(ele.val / 2)), Integer(ceil(ele.val / 2))]
                return True

    while True:
        flat_snum = list(flatten(snum))
        if explode(snum, flat_snum, 1):
            continue
        if split(snum, flat_snum, 1):
            continue
        break

    return snum


def add(snum1, snum2):
    return [snum1, snum2]


def part1(data):
    snum1, snum2 = (toInteger(eval(data[0].strip())), toInteger(eval(data[1].strip())))
    result = add(snum1, snum2)
    reduce(result)

    for line in data[2:]:
        new_snum = toInteger(eval(line.strip()))
        result = add(result, new_snum)
        reduce(result)

    return magnitude(result)


def part2(snums):
    return max(
        magnitude(reduce(add(deepcopy(snum1), deepcopy(snum2))))
        for snum1 in snums
        for snum2 in snums
    )
