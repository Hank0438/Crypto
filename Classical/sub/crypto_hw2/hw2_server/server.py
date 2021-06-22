# !/usr/bin/python3.6
# -*- coding: utf-8 -*-


import random
import string
from hashlib import md5
import re
import base64
import os

with open('./plain.txt') as f:
    plain = f.read()
with open('./secret.txt') as f:
    secret = f.read()
with open('./flag.txt') as f:
    flag = f.read()

registered = {}

def genPlaintext():
    rndgen = random.SystemRandom()
    start = int((len(plain) - 10001) * rndgen.random())
    show = plain[start:start + 10000]
    return show

def genToken(sid):
    answer = sid + secret
    answer = md5(answer.encode("utf-8")).digest()
    answer = str(base64.b64encode(answer))
    answer = re.sub(r'\W+', '', answer)
    answer = re.sub(r'\d+', '', answer).upper()
    registered[sid] = 1
    return answer
    
def genCiphertext(text):
    org = string.ascii_uppercase
    key = list(org)
    random.shuffle(key)
    mappingTable = {"{":"{", "}":"}"}
    for i in range(26):
        mappingTable[chr(65+i)] = key[i]
        mappingTable[chr(97+i)] = key[i]

    chipher = ""
    for x in text:
        chipher += mappingTable[x]

    return chipher

while True:
    print(f'[?] Available commands: register, login')
    cmd = input('[>] ')
    if cmd == 'register':
        iswarrior = input("[>] Warrior Mode (y/n): ")
        if iswarrior == 'n':
            sid = input("[>] your student number: ")
            token = genToken(sid)
            plaintext = genPlaintext()
            plaintext = "{" + token + "}" + plaintext
            print("plaintext:", plaintext[:100])
            chiphertext = genCiphertext(plaintext)
            print("chiphertext: ", chiphertext)
        elif iswarrior == 'y':
            sid = input("[>] your student number: ")
            token = genToken(sid)
            plaintext = genPlaintext()
            plaintext = "{" + token + "}" + plaintext

    '''
    elif cmd == 'login':
        print(f'[+] {flag}')

        sid = input("[>] your student number: ")
        token = input('[>] Token: ')

        secret = 'Crypto is fun' + sid + key
        mac2 = md5(secret.encode("utf-8")).digest()
        if mac2 != mac:
            print(f'[!] Invalid mac')
        elif sid not in registered:
            print(f'[+] {flag}')
        else:
            print(f'[!] Try harder')
    '''
