import binascii

# given string (in hex)
str_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# string converted to binary from hex
str_bin = binascii.unhexlify(str_hex)
# string converted to base64 from binary
str_base64 = binascii.b2a_base64(str_bin)
# final string decoded to UTF-8 and stripped off that newline
str_fin = str_base64.decode().replace('\n','')

print(str_fin)