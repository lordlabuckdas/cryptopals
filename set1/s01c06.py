import base64


def get_hamming_dist(str1, str2):
    dist = 0
    for i, j in zip(str1, str2):
        #x = ord(i)^ord(j)
        x = i ^ j
        set_bits = 0
        while x > 0:
            set_bits += x & 1
            x >>= 1
        dist += set_bits
    return dist


def get_top3_keysizes(msg):
    norm_dists = {}
    for keysize in range(2,41):
        str1 = msg[:keysize]
        str2 = msg[keysize:2*keysize]
        norm_dist = get_hamming_dist(str1, str2)/keysize
        norm_dists[norm_dist] = keysize
    return [j for i,j in sorted(norm_dists.items())[:3]]


if __name__ == "__main__":
    # parse related file
    f = open('set1/6.txt')

    msg = f.read()
    msg = base64.b64decode(msg)

    keysizes = get_top3_keysizes(msg)

    f.close()

# import base64
# from s01c03 import char_freq, xor_1byte_bruteforce

# def get_hamming_dist(str1, str2):
#     dist = 0
#     for i, j in zip(str1, str2):
#         x = ord(i)^ord(j)
#         set_bits = 0
#         while x > 0:
#             set_bits += x & 1
#             x >>= 1
#         dist += set_bits
#     return dist


# def get_top3_keysizes(msg):
#     norm_dists = {}
#     for keysize in range(2,41):
#         str1 = msg[: keysize]
#         str2 = msg[keysize : 2 * keysize]
#         norm_dist = get_hamming_dist(str1, str2) / keysize
#         norm_dists[norm_dist] = keysize
#     return [j for i,j in sorted(norm_dists.items())[:3]]


# def break_n_transpose(msg, keysize):
#     temp_blocks = [msg[i * keysize : (i + 1) * keysize] for i in range(len(msg) // keysize)]
#     msg_blocks = []
#     i=0
#     j=0
#     while j < keysize:
#         temp_str = ''
#         while i < len(temp_blocks):
#             temp_str += msg[i][j]
#             i += 1
#         msg_blocks.append(temp_str)
#         j += 1

#     return msg_blocks


# def xor_1byte_get_key(str1, str2):
#     key = bytearray(ord(a) ^ ord(b) for a, b in zip(str1, str2))
#     return key

# if __name__ == "__main__":
#     # parse related file
#     f = open('set1/6.txt')

#     msg = f.read()
#     msg = base64.b64decode(msg).decode()

#     keysizes = get_top3_keysizes(msg)

#     for keysize in keysizes:
#         msg_blocks = break_n_transpose(msg, keysize)
#         for block in msg_blocks:
#             poss_chars = xor_1byte_bruteforce(block)
#             poss_chars = sorted(poss_chars.items(), key=lambda e: e[1], reverse=True)[:3]
#             key = xor_1byte_get_key(poss_chars[0][0], block)
#             print(key)


#     f.close()

    

