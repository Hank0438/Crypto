import sys
import random
import z3
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encrypt():
    key = 'Crypto-is-fun'
    flag = 'Crypto{this_is_a_simple_encryption}'

    assert len(key) == 13
    assert max([ord(char) for char in key]) < 128
    assert max([ord(char) for char in flag]) < 128

    message = flag + "|" + key

    encrypted = chr(random.randint(0, 128))

    for i in range(0, len(message)):
        encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)

    print(hex(bytes_to_long(encrypted.encode())))

def decrypt():
    data = long_to_bytes(0xa107466462e0c34116c025b2f063c0d67361d750f6847591e78547a5e503018700c63537c250c73260c74116e502a79617c)
    s = z3.Solver()
    flag = [z3.Int("flag_" + str(i)) for i in range(len(data) - 15)]
    key = [z3.Int("key_" + str(i)) for i in range(13)]
    pipe = z3.Int("pipe")
    s.add(pipe == ord("|"))
    for var in flag:
        s.add(var < 128)
        s.add(var >= 0)
    for i, c in enumerate("Crypto{"):
        s.add(flag[i] == ord(c))
    for var in key:
        s.add(var < 128)
        s.add(var >= 0)
    message = flag + [pipe] + key
    for i in range(1, len(data)):
        index = i - 1
        byte = data[i]
        s.add((message[index] + key[index % 13] + data[index]) % 128 == byte)
    print(s.check())
    print(s.model())
    print("".join([chr(int(str(s.model()[var]))) for var in message]))

encrypt()
decrypt()