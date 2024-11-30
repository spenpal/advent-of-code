from collections import Counter


def parse(data: str) -> dict[int, tuple]:
    template = data.split("\n\n")[0].strip()

    rules = {}
    for line in data.split("\n\n")[1].splitlines():
        search, insert = line.strip().split(" -> ")
        rules[search] = insert

    return {1: (template, rules), 2: (template, rules)}


def part1(template, rules):
    polymer = template
    for step in range(10):
        polymer_copy = []
        for idx in range(len(polymer) - 1):
            pair = polymer[idx : idx + 2]
            polymer_copy.append(f"{pair[0]}{rules[pair]}")
        polymer = "".join([new_pair for new_pair in polymer_copy]) + polymer[-1]

    word_counts = Counter(polymer)
    most_common_count = word_counts.most_common()[0][1]
    least_common_count = word_counts.most_common()[-1][1]

    return most_common_count - least_common_count


def part2(template, rules):
    def insertion(pair, step, mem, counts, rules):
        if step == 0:
            return

        insert = rules[pair]
        counts[insert] += 1

        new_polymer = f"{pair[0]}{insert}{pair[1]}"
        pair1, pair2 = new_polymer[:2], new_polymer[1:]

        for new_pair in [pair1, pair2]:
            key = (new_pair, step)
            if key in mem:
                counts.update(mem[key])
            else:
                prev_counts = counts.copy()
                insertion(new_pair, step - 1, mem, counts, rules)
                mem[key] = counts - prev_counts

    polymer = template
    counts = Counter(polymer)

    pairs = [polymer[idx : idx + 2] for idx in range(len(polymer) - 1)]
    for pair in pairs:
        insertion(pair, 40, {}, counts, rules)

    most_common_count = counts.most_common()[0][1]
    least_common_count = counts.most_common()[-1][1]

    return most_common_count - least_common_count
