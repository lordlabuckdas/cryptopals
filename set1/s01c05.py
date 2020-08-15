import binascii


def xor_repeating_key(msg, key):
    # create the ascii version of the encrypted msg by xor-ing
    str_asc = ''.join(chr(ord(msg[i])^ord(key[i%3])) for i in range(len(msg)))
    return str_asc


if __name__ == "__main__":    
    msg = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

    key = 'ICE'

    str_asc = xor_repeating_key(msg, key)

    # conversion to hex
    encrypted_msg = binascii.hexlify(str_asc.encode())

    print(encrypted_msg.decode())