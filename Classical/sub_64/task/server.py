#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

import random
import string
from hashlib import md5
import re
import base64
import os
import sys

with open('./plain.txt') as f:
    plain = f.read()
with open('./secret2.txt') as f:
    flag = f.read()

registered = {}

def genPlaintext():
    rndgen = random.SystemRandom()
    start = int((len(plain) - 10001) * rndgen.random())
    show = plain[start:start + 10000]
    return show

    
def genCiphertext(text):
    key = list(range(26))
    random.shuffle(key)
    cipher = ""
    for x in text:
        if (ord(x) >= 65) & (ord(x) <= 90):
            cipher += chr(65 + key[ord(x)-65])
        elif (ord(x) >= 97) & (ord(x) <= 122):
            cipher += chr(97 + key[ord(x)-97])
        else:
            cipher += x

    return cipher

if '__name__' != '__main__':
    
    plaintext = genPlaintext()
    plaintext = flag + plaintext
    plaintext = plaintext.encode()
    plaintext = base64.b64encode(plaintext)
    plaintext = plaintext.decode()
    
    chiphertext = genCiphertext(plaintext)
    print("chiphertext: ", chiphertext)
    sys.stdout.flush()
    exit(0)
    
    
