bytestr = bytes(b'\n\n`\xaa\xdb\x93')
print(len(bytestr))

for i in bytestr:
    print(i, end=" ")

# 10 10 96 170 219 147
# Nanoseconds = 147 + 219 * (2^8) + 170 * (2 ^ 16) + 96 * (2 ^ 24) + 10 * (2 ^ 32) + 10 * (2 ^ 40)
# Seconds = 11039.6877608

"""
b'S' b'\x00\x00\x00\x00\n\n`\xaa\xdb\x93O'
b'R' b'\x00\x01\x00\x00\nJL\xeeU\x99A       N \x00\x00\x00dNCZ PN 1N\x00\x00\x00\x00N'
b'R' b'\x00\x02\x00\x00\nJM\x06--AA      N \x00\x00\x00dNCZ PN 1N\x00\x00\x00\x01N'
b'R' b'\x00\x03\x00\x00\nJM\x07\x01oAAAU    P \x00\x00\x00dNQI PN 2Y\x00\x00\x00\x01N'
b'R' b'\x00\x04\x00\x00\nJM\x07\xb0\x96AABA    QN\x00\x00\x00dNCQ PNN2N\x00\x00\x00\x01N'
b'R' b'\x00\x05\x00\x00\nJM\x08\x85lAAC     N \x00\x00\x00dNCZ PN 2N\x00\x00\x00\x00N'
"""