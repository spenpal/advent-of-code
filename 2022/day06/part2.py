with open("input.txt") as f:
    data = f.readline()
    window_length = 14
    i = 0
    while i <= len(data)-window_length:
        four_letters = data[i:i+window_length]
        if len(set(four_letters)) == window_length: break
        i += 1
            
print(i+window_length)