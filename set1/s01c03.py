def char_freq(poss_str):
    # function to check the char frequency of alphabets
    # number of alphabets stored in num_valid_chars
    num_valid_chars = list(
        filter(lambda e: 'A' <= e <= 'Z' or 'a' <= e <= 'z', poss_str))
    # poss_str with the highest ratio will be the most accurate
    if len(poss_str)!=0:
        return float(len(num_valid_chars))/len(poss_str)
    else:
        return 0


def xor_1byte_bruteforce(str_asc):
    # initializing dictionary with the possible strings and their accuracy
    poss_strs = {}
    # loop through all 256 ascii chars and
    # xor-ing with each letter of given string in ascii
    # then create item with string as key and accuracy as value
    for i in range(256):
        poss_str = ''.join(chr(ord(a) ^ i) for a in str_asc)
        poss_strs[poss_str] = char_freq(poss_str)
    # return poss_strs
    return poss_strs


if __name__ == "__main__":
    # given string
    str_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # string converted from hex to ascii
    str_asc = bytearray.fromhex(str_hex).decode()

    poss_strs = xor_1byte_bruteforce(str_asc)

    # most accurate string
    orig_str = sorted(poss_strs.items(), key=lambda e: e[1], reverse=True)[0][0]

    print('decrypted msg: ' + orig_str)

    # key that was xor-ed with
    msg_key = list(poss_strs.keys()).index(orig_str)

    print('key: ' + chr(msg_key))
