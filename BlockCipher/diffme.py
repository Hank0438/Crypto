#!/usr/bin/python
"""
 Disclaimer
	The encryption algorithm included in this file is not be used for the protection of information. It is merely purposed to aid education.
	The author does not except any responisiblity for its use.
- Keith Makan
"""
from random import random
import struct

class DiffMe:
	def __init__(self,plain_text,key):
			self.plaintext = plain_text
			self.key = key	
			self.sbox = [3,14,1,10,4,9,5,6,8,11,15,2,13,12,0,7] #4 bit SBOX
			self.convert_to_padded_bin = lambda x: "%08i" % (int(bin(x)[2:])) #lols a little formatting hack
	"""
		Round function:
			Basically runs the data XOR key through the SBox,
			data - integer of plaintext (4bit) 0000 - 1111
			key  - integer of the key   (4bit) 
	"""
	def round_func(self,data,key): #feelin funcy :)
		return self.sbox[key ^ data]
	def _encrypt(self,data,k0,k1):
		x0 = self.round_func(data,k0)
		#print "%x" % (x0 ^ k1)
		return int(x0 ^ k1)
	"""
		little helper function to split the key up into subkeys
	"""	
	def split_key(self,key):
		k1 = self.convert_to_padded_bin(key)[4:]
		k2 = self.convert_to_padded_bin(key)[:4]
		return int(k2),int(k1)
	"""
		encrypt the wrapper function that takes in strings and processes each character using the round functoin
		string - a string of arbtirary length to be encrypted
		key  - a 16 (8byte) key that gets split into 4byte halfs	(in pythonic terms this is a list of integers)
	"""
	def encrypt(self,string,key):
		#we need to encrypt every 4 bitsk = split_key(key)
		binlist = self.string_to_bin(string)
		k = self.split_key(key)
		return [ self._encrypt(int(c,2),k[0],k[1]) for c in binlist]
	"""
		string_to_bin - convers strings to lists of 4bit binary values
	"""		
	def string_to_bin(self,string):
		#make a list of 4 bit binary strings from a string
		bin_string = list(''.join([ self.convert_to_padded_bin(ord(c)) for c in string]))
		temp = ""
		outlist = []
		for c in bin_string:
			temp += c
			if len(temp) == 4:
				outlist.append(temp)
				temp = ""
		return outlist	
if __name__ == "__main__":
	diff = DiffMe(None,None)
	while True:
		key = int(random()*999)%2**4
		k0,k1 = diff.split_key(key)
		diff.key = key
		print "key     : ",key
		print "encrypt : ",diff._encrypt(input(">"),k0,k1)
		#print "encrypt :",diff.encrypt(input(">"),key)