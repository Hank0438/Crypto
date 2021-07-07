#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

import random
import string
from hashlib import md5
import re
import base64
import os
import sys

with open('/home/sub/plain.txt') as f:
    plain = f.read()
with open('/home/sub/secret1.txt') as f:
    secret1 = f.read()
with open('/home/sub/secret2.txt') as f:
    secret2 = f.read()

registered = {}

def genPlaintext():
    rndgen = random.SystemRandom()
    start = int((len(plain) - 10001) * rndgen.random())
    show = plain[start:start + 10000]
    return show

def genToken(sid, secret):
    answer = sid + secret
    answer = md5(answer.encode("utf-8")).digest()
    answer = str(base64.b64encode(answer))
    answer = re.sub(r'\W+', '', answer)
    answer = re.sub(r'\d+', '', answer).upper()
    registered[sid] = 1
    return answer
    
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
    
    sid = input("[>] your student number: ").strip()
    isbase64 = input("[>] Do you want some base64 (y/n): ").strip()
    if isbase64 == "y":
        token = genToken(sid, secret2)
        plaintext = genPlaintext()
        plaintext = "{" + token + "}" + plaintext
        plaintext = plaintext.encode()
        plaintext = base64.b64encode(plaintext)
        plaintext = plaintext.decode()
    else:
        token = genToken(sid, secret1)
        plaintext = genPlaintext()
        plaintext = "{" + token + "}" + plaintext
    chiphertext = genCiphertext(plaintext)
    print("chiphertext: ", chiphertext)
    sys.stdout.flush()
    exit(0)
    
    
