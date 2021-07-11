import sys
import random
import z3
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encrypt(key, flag):

    message = flag + "|" + key

    encrypted = chr(random.randint(0, 128))

    for i in range(0, len(message)):
        encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)

    print(hex(bytes_to_long(encrypted.encode())))

def decrypt():
    pass


key = open("key.txt", "r").read().strip()
flag = open("flag.txt", "r").read().strip()
assert len(key) == 13
assert max([ord(char) for char in key]) < 128
assert max([ord(char) for char in flag]) < 128

encrypt(key, flag)