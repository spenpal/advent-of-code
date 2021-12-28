def part1(bnums):
    gamma_bin, epsilon_bin = [], []
    bits_length = len(bnums[0])
    bits = {'0', '1'}
    
    for bit_position in range(bits_length):
        position_bits = [bnum[bit_position] for bnum in bnums]
        most_common_bit = max(bits, key = position_bits.count)
        least_common_bit = '0' if most_common_bit == '1' else '1'
        gamma_bin.append(most_common_bit)
        epsilon_bin.append(least_common_bit)
    
    gamma_bin, epsilon_bin = ''.join(gamma_bin), ''.join(epsilon_bin)
    gamma_dec, epsilon_dec = int(gamma_bin, 2), int(epsilon_bin, 2)
    return gamma_dec * epsilon_dec

def part2(bnums):
    from collections import Counter
    
    oxygen_generator_bnums, co2_scrubber_bnums = bnums.copy(), bnums.copy()
    
    bit_position = 0
    while len(oxygen_generator_bnums) > 1:
        position_bits = [bnum[bit_position] for bnum in oxygen_generator_bnums]
        most_common_bits = Counter(position_bits).most_common()
        
        if most_common_bits[0][1] == most_common_bits[1][1]:
            oxygen_generator_bnums = [bnum for bnum in oxygen_generator_bnums if bnum[bit_position] == '1']
        else:
            most_common_bit = most_common_bits[0][0]
            oxygen_generator_bnums = [bnum for bnum in oxygen_generator_bnums if bnum[bit_position] == most_common_bit]
        
        bit_position += 1
    
    bit_position = 0
    while len(co2_scrubber_bnums) > 1:
        position_bits = [bnum[bit_position] for bnum in co2_scrubber_bnums]
        most_common_bits = Counter(position_bits).most_common()
        
        if most_common_bits[0][1] == most_common_bits[1][1]:
            co2_scrubber_bnums = [bnum for bnum in co2_scrubber_bnums if bnum[bit_position] == '0']
        else:
            least_common_bit = most_common_bits[1][0]
            co2_scrubber_bnums = [bnum for bnum in co2_scrubber_bnums if bnum[bit_position] == least_common_bit]
            
        bit_position += 1
    
    [oxygen_generator_bnum], [co2_scrubber_bnum] = oxygen_generator_bnums, co2_scrubber_bnums
    oxygen_generator_dnum, co2_scrubber_dnum = int(oxygen_generator_bnum, 2), int(co2_scrubber_bnum, 2)
    return oxygen_generator_dnum * co2_scrubber_dnum
            
def main():
    with open("puzzle_input.txt") as f:
        bnums = f.read().splitlines()
        
    print(f"Part 1 Answer: {part1(bnums)}")
    print(f"Part 2 Answer: {part2(bnums)}")

if __name__ == "__main__":
    main()