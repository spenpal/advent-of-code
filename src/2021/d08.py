def parse(data: str) -> dict[int, tuple]:
    input = data.splitlines()
    input = [entry.split("|") for entry in input]
    input = [[pattern.split(), output.split()] for pattern, output in input]
    return {1: (input,), 2: (input,)}


def unique_digit(digit):
    return len(digit) in {2, 3, 4, 7}


def encode(pattern):
    signal_mapping = dict.fromkeys("abcdefg", "")

    [digit1] = [digit for digit in pattern if len(digit) == 2]
    [digit3] = [
        digit for digit in pattern if len(digit) == 5 and set(digit1) < set(digit)
    ]
    [digit4] = [digit for digit in pattern if len(digit) == 4]
    [digit6] = [
        digit for digit in pattern if len(digit) == 6 and not set(digit1) < set(digit)
    ]
    [digit7] = [digit for digit in pattern if len(digit) == 3]
    [digit8] = [digit for digit in pattern if len(digit) == 7]

    [a_map_let] = list(set(digit7) - set(digit1))
    signal_mapping[a_map_let] = "a"
    [g_map_let] = list(set(digit3) - (set(digit4) | set(a_map_let)))
    signal_mapping[g_map_let] = "g"
    [d_map_let] = list(set(digit3) - (set(digit7) | set(g_map_let)))
    signal_mapping[d_map_let] = "d"
    [b_map_let] = list(set(digit4) - (set(digit1) | set(d_map_let)))
    signal_mapping[b_map_let] = "b"
    [e_map_let] = list(set(digit8) - (set(digit3) | set(b_map_let)))
    signal_mapping[e_map_let] = "e"
    [c_map_let] = list(set(digit8) - set(digit6))
    signal_mapping[c_map_let] = "c"
    [f_map_let] = list(set(digit1) - set(c_map_let))
    signal_mapping[f_map_let] = "f"

    return signal_mapping


def decode(input, encoder):
    return "".join(encoder[let] for let in input)


def part1(input):
    return sum(sum(unique_digit(digit) for digit in outputs) for _, outputs in input)


def part2(input):
    output_values_sum = 0
    seg2num = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    for pattern, output in input:
        encoder = encode(pattern)
        decoded_num = []
        for seg in output:
            decoded_seg = "".join(sorted(decode(seg, encoder)))
            decoded_digit = seg2num[decoded_seg]
            decoded_num.append(decoded_digit)
        output_values_sum += int("".join(decoded_num))

    return output_values_sum
