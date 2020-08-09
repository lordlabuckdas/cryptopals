import binascii

str_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
str_bin = binascii.unhexlify(str_hex)
str_base64 = binascii.b2a_base64(str_bin)
str_fin = str_base64.decode().replace('\n','')

print(str_fin)