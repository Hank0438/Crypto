#!/usr/bin/python

import random
import gmpy2
import sys
from Crypto.Util.number import long_to_bytes, bytes_to_long

def makeKey(n):
	privKey = [random.randint(1, 4**n)]
	s = privKey[0]
	for i in range(1, n):
		privKey.append(random.randint(s + 1, 4**(n + i)))
		s += privKey[i]
	q = random.randint(privKey[n-1] + 1, 2*privKey[n-1])
	r = random.randint(1, q)
	while gmpy2.gcd(r, q) != 1:
		r = random.randint(1, q)
	pubKey = [ r*w % q for w in privKey ]
	return privKey, q, r, pubKey

def encrypt(msg, pubKey):
	msg_bit = msg
	n = len(pubKey)
	cipher = 0
	i = 0
	for bit in msg_bit:
		cipher += int(bit)*pubKey[i]
		i += 1
	return bin(cipher)[2:]

def decrypt(cipher, privKey, q, r):
	s = gmpy2.invert(r, q)
	cipher = int(cipher, 2)
	msg = cipher*s % q
	res = ''
	n = len(privKey)
	for i in range(n - 1, -1, -1):
		if msg >= privKey[i]:
			res = '1' + res
			msg -= privKey[i]
		else:
			res = '0' + res 
	return res

f_pubKey = open("pubKey.txt", "w")
f_enc = open("enc.txt", "w")
secret = open("./flag.txt", "rb").read().strip()

msg_bit = bin(bytes_to_long(secret))[2:]
keyPair = makeKey(len(msg_bit))
f_pubKey.write(f"L, ".join([str(k) for k in keyPair[3] ]))
enc =  encrypt(msg_bit, keyPair[3])
f_enc.write(f'{int(enc, 2)}')

