#!/usr/bin/python3
from Crypto.Cipher import DES
import binascii
import itertools
import random
import string

# weak_key = b"\x01\x01\x01\x01\x01\x01\x01\x01"
weak_key = b"\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE"

msg = "abcdefgh".encode()
cipher1 = DES.new(weak_key, DES.MODE_ECB)
enc_msg1 = cipher1.decrypt(msg)
print(enc_msg1)
enc_msg2 = cipher1.decrypt(enc_msg1)
print(enc_msg2)

def xgcd(a, b):
    """
    Extented Euclid GCD algorithm.
    Return (x, y, g) : a * x + b * y = gcd(a, b) = g.
    """
    if a == 0: return 0, 1, b
    if b == 0: return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a
a, b, c = xgcd(5**7, 7**5)
print(a+b)