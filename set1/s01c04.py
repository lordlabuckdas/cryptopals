from s01c03 import char_freq, xor_1byte_bruteforce

if __name__ == "__main__":
    with open('set1/4.txt') as f:
        # read from the file and store as a list
        arr_lines = f.read().split('\n')


    # initializing dictionary with the most accurate string of each line and their accuracy
    poss_lines = {}

    for line in arr_lines:
        try:
            # for errors related to decoding from hex
            str_asc = bytearray.fromhex(line).decode()
            poss_strs = xor_1byte_bruteforce(str_asc)
            # getting the most accurate pair
            x, y = sorted(poss_strs.items(), key=lambda e: e[1], reverse=True)[0]
            poss_lines[x] = y
        except:
            pass

    # sort it
    poss_lines = sorted(poss_lines.items(), key=lambda e: e[1], reverse=True)

    # this time, the second string is the decrypted msg
    print(poss_lines[1][0])
