import binascii

def xor_byte2byte(str1_bin, str2_bin):
    # function to xor the 2 binary strings
    if len(str1_bin) != len(str2_bin):
        # because fixed length xor
        return
    # xor byte to byte and form bytearray to store them all
    return bytearray(a ^ b for a, b in zip(str1_bin, str2_bin))

if __name__ == "__main__":
    # given strings
    str1_hex = "1c0111001f010100061a024b53535009181c"
    str2_hex = "686974207468652062756c6c277320657965"

    try:
        str1_bin = binascii.unhexlify(str1_hex)
        str2_bin = binascii.unhexlify(str2_hex)
    except:
        print('String of odd length')
        exit()

    try:
        str_fin_bin = binascii.hexlify(xor_byte2byte(str1_bin, str2_bin))
    except:
        print('Unequal length')
        exit()

    # finally convert bytearray to UTF-8
    print(str_fin_bin.decode())
