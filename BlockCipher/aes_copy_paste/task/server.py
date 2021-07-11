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

FLAG = open("./flag.txt", "r").read().strip()
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


def alarm(time):

	signal.signal(signal.SIGALRM, lambda signum, frame: bye('Too slow!'))
	signal.alarm(time)


def printFlag():
	print(FLAG)


def register():

	name = input('What is your name? ').strip()

	for c in name:
		if c not in string.ascii_letters:
			bye('Invalid characters.(Only alphabets are permitted)')

	pwd = input('Give me your password: ').strip()

	for c in pwd:
		if c not in string.ascii_letters:
			bye('Invalid characters. (Only alphabets are permitted)')

	pattern = 'name=' + name + '&role=student' + '&password=' + pwd

	token = b64e(aes.encrypt(pattern.encode())).decode()

	print('This is your token: ', token)
	return token


def login():

	token = input('Give me your token: ').strip()
	name = input('Give me your username: ').strip()
	pwd = input('Give me your password: ').strip()

	try:
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

	except Exception:
		print('Something went wrong!! QAQ')



def main():

	alarm(100)
	for _ in range(3):
		print('Select your choice: ')
		print('0 : Register')
		print('1 : Login')

		num = int(input().strip())
		if num == 0:
			register()
		elif num == 1:
			login()


if __name__ == '__main__':

	main()