#!/usr/bin/python3 -u
from pwn import *

from Crypto.Cipher import DES
import itertools
import string

KEY_LEN = 5

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def double_decrypt(m, key1, key2):
    cipher2 = DES.new(key2, DES.MODE_ECB)
    dec_msg = cipher2.decrypt(m)

    cipher1 = DES.new(key1, DES.MODE_ECB)
    return cipher1.decrypt(dec_msg)

def all_possible_keys():
    return itertools.product(string.digits, repeat=KEY_LEN)


encrypted_flag = "81364f5a6e25f2c7da21310e077508fdc865f65fd58c37445c1ab90c3edebdd8272fdf26f5975ffe7e4270fe6a67999f"
encrypted_a = "ec4f5e7014bc9cb3"

to_encrypt = b'a'
a_enc = bytes.fromhex(encrypted_a)

a_padded = pad(to_encrypt.decode())

d = {}

with log.progress('Encrypting plaintext with all possible keys') as p:
    for k1 in all_possible_keys():
        k1 = pad("".join(k1))
        p.status("Key: {}".format(k1))
        cipher1 = DES.new(k1, DES.MODE_ECB)
        enc = cipher1.encrypt(a_padded)
        d[enc] = k1

with log.progress('Decrypting ciphertext with all possible keys') as p:
    for k2 in all_possible_keys():
        k2 = pad("".join(k2))
        p.status("Key: {}".format(k2))
        cipher2 = DES.new(k2, DES.MODE_ECB)
        dec = cipher2.decrypt(a_enc)
        if dec in d:
            k1 = d[dec]
            log.info("Found match, key1 = {}, key2 = {}".format(k1, k2))
            log.success(double_decrypt(unhex(encrypted_flag), k1, k2))
            break
            