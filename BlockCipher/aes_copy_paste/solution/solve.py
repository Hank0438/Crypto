#!/usr/bin/python3
import signal
import sys
import os
import time
import string
from urllib.parse import parse_qs
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

FLAG = "ais3{ABCDEFGHIJKLMNOPQRSTUVWXYZZZZZZZ}"
KEY = get_random_bytes(32)

blockSize = 16

class AESCryptor:

	def __init__(self, key):

		self.KEY = key
		self.aes = AES.new(self.KEY, AES.MODE_ECB)


	def encrypt(self, data):
		print(self.pad(data))
		return self.aes.encrypt(self.pad(data))


	def decrypt(self, data):
		print(data)

		return self.unpad(self.aes.decrypt(data))

	def pad(self, data):
		num = blockSize - len(data) % blockSize
		return data + bytes([num]) * num

	def unpad(self, data):

		lastValue = 0
		print(data)

		if type(data[-1]) is int:
			lastValue = data[-1]
		else:
			lastValue = ord(data[-1])

		return data[:len(data)-lastValue]


aes = AESCryptor(KEY)


def bye(s):
	print(s)
	exit(0)


# def alarm(time):

# 	signal.signal(signal.SIGALRM, lambda signum, frame: bye('Too slow!'))
# 	signal.alarm(time)


def printFlag():
	print(FLAG)


def register(name, pwd):

	# name = input('What is your name? ').strip()

	for c in name:
		if c not in string.ascii_letters:
			bye('Invalid characters.(Only alphabets are permitted)')

	# pwd = input('Give me your password: ').strip()

	for c in pwd:
		if c not in string.ascii_letters:
			bye('Invalid characters. (Only alphabets are permitted)')

	pattern = 'name=' + name + '&role=student' + '&password=' + pwd

	token = b64e(aes.encrypt(pattern.encode())).decode()

	print('This is your token: ', token)
	return token


def login(name, pwd, token):

	# token = input('Give me your token: ').strip().encode()
	# name = input('Give me your username: ').strip().encode()
	# pwd = input('Give me your password: ').strip().encode()

	
	pt = aes.decrypt(b64d(token.encode())).decode()
	data = parse_qs(pt, strict_parsing=True)

	if name != data['name'][0] or pwd != data['password'][0]:
		print('Authentication failed')
		return

	print(f"Hello {data['name'][0]}")
	print(data)

	if 'admin' in data['role']:
		print('Hi admin:')
		printFlag()

	# except Exception:
	# 	print('Something went wrong!! QAQ')



def main():

	# alarm(60)
	print('Select your choice: ')
	print('0 : Register')
	print('1 : Login')

	# num = int(input().strip())
	# if num == 0:
	# 	register()
	# elif num == 1:
	# 	login()

	name = 'AAAAA'
	pwd = 'abcde'
	fake_name = 'AAAAABBBBBBadmin'
	
	token = register(name, pwd)
	fake_token = register(fake_name, pwd)

	token_b64d = b64d(token.encode())
	fake_token_b64d = b64d(fake_token.encode())
	fake_token = b64e(token_b64d[0:16] + fake_token_b64d[16:]).decode()





	login(name, pwd, token)
	login(name, pwd, fake_token)


if __name__ == '__main__':

	# main()
    while(1):
        a = input('Give me your token: ').strip()
        b = input('Give me your token: ').strip()

        a1 = b64d(a.encode())
        b1 = b64d(b.encode())
        print(b64e(a1[:16]+b1[16:]).decode())