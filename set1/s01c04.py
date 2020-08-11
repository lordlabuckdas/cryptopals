with open('set1/4.txt') as f:
    # read from the file and store as a list
    arr_lines = f.read().split('\n')


def char_freq(poss_str):
    # function to check the char frequency of alphabets
    # number of alphabets stored in num_valid_chars
    num_valid_chars = list(
        filter(lambda e: 'A' <= e <= 'Z' or 'a' <= e <= 'z', poss_str))
    # poss_str with the highest ratio will be the most accurate
    return float(len(num_valid_chars))/len(poss_str)


# initializing dictionary with the most accurate string of each line and their accuracy
poss_lines = {}

for line in arr_lines:
    try:
        # for errors related to decoding from hex
        str_asc = bytearray.fromhex(line).decode()
        # initializing dictionary with the possible strings and their accuracy
        poss_strs = {}
        # loop through all 256 ascii chars and
        # xor-ing with each letter of given string in ascii
        # then create item with string as key and accuracy as value
        for i in range(256):
            poss_str = ''.join(chr(ord(a) ^ i) for a in str_asc)
            poss_strs[poss_str] = char_freq(poss_str)
        # getting the most accurate pair
        x, y = sorted(poss_strs.items(), key=lambda e: e[1], reverse=True)[0]
        poss_lines[x] = y
    except:
        pass

# sort it
poss_lines = sorted(poss_lines.items(), key=lambda e: e[1], reverse=True)

# this time, the second string is the decrypted msg
print(poss_lines[1][0])
