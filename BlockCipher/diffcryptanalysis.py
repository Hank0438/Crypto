#!/usr/bin/python
from diffme import DiffMe
from random import random
#build a map of input-outpu differentials
"""
	this little script performs differential cryptanalysis of the DiffMe cipher.
	
	Here's how it works:
		1. It bulids a matrix of all the possible inputs that correlates the XOR differences
		2. using this it builds a dictionary of input differentials (XOR differences) mapped to output differentials
		3. once this is dictionary is available, it then runs through all the possible input output pairs and finds "good pairs"
		4. using these good pairs it attacks a crypto system to derive the key.
"""
class DiffCryptAnalysis:
	def __init__(self,sboxes,pairs):
		self.sboxes = sboxes #the sboxes to be analyzed, in future this should probably be wrapped in an object
		"""
			the differential dictionary
			each association in the dictionary is of the form:
				"%s :=> %s" % (i^j,sbox[i]^sbox[j]) :=> [COUNT,
																			[
																				[(x_i,y_i),(x_o,y_o)],[(),()],...
																			]
																	 ]
								^
				Where:
						- COUNT is the number of times this differential occurs; the rest of the element is a list of pairs that satisfy the differential
						- x_i,y_i is the input pair
						- x_o,y_o is the output pair
						
				*the dictionary keys are designed to document the diffentials i.e. the input XOR difference that maps to the XOR output differnce
				*each element documents the number of times a differential is satisfied as well as the input/output pairs that satisfy the differential
		> look you can come up with your own crazy data structure to handle this information, but as far as I know this is the simplest and most functional design i could come up with, in like 2 hours.				  
		"""
		self.differentials = {} #a dictionary of differentials, the whole point of this class is to build this dictionary, maybe we could make this a heap? auto prioritize the most probably keys? No! only look for efficiencey when its needed, otherwise focus on solving the problem first ;)
		self.text_pairs = pairs #
		self.diff_pairs = [] #XOR differences between plaint-text/cipher-text pairs
	def build_differentials(self):
		self.differentials = {}
		for sbox in self.sboxes:
			for i in range(len(sbox)): 
				for j in range(i+1,len(sbox)):
					#print "[%s:%s]" % (i,j), i^j, "delta: ",sbox[i^j]	
					try:
						self.differentials["%s :=> %s" % (i^j,sbox[i]^sbox[j])][1].append([(i,j),(sbox[i],sbox[j])])
						self.differentials["%s :=> %s" % (i^j,sbox[i]^sbox[j])][0]+=1
					except KeyError:
						self.differentials["%s :=> %s" % (i^j,sbox[i]^sbox[j])] = [1,[[(i,j),(sbox[i],sbox[j])]]]
	"""
		Given a pairs of plain-text/cipher-texts find a list of the most probable sbox input output pairs
			
	"""
	def findSBoxIOs(self):
		return []
	def getPairDifferentials(self):
		#text_pairs[0] = list of inputs
		#text_pairs[1] = list of ouputs	
		diffs = {}
		for i in range(len(self.text_pairs[0])):
			for j in range(i+1,len(self.text_pairs[0])): 
				try:
					diffs["%s :=> %s" % (self.text_pairs[0][i]^self.text_pairs[0][j],self.text_pairs[1][i]^self.text_pairs[1][j])].append([(self.text_pairs[0][i],self.text_pairs[0][j]),(self.text_pairs[1][i],self.text_pairs[1][j])])
				except KeyError:	
					diffs["%s :=> %s" % (self.text_pairs[0][i]^self.text_pairs[0][j],self.text_pairs[1][i]^self.text_pairs[1][j])] = [[(self.text_pairs[0][i],self.text_pairs[0][j]),(self.text_pairs[1][i],self.text_pairs[1][j])]]
		return diffs
if __name__ == "__main__":	
	diff = DiffMe(None,None)	
	inputs = [int(random()*1000)%10 for i in range(10) ] #lols I know there are some security researchers who almost got a heart attack coz I used random() :P
	k0,k1 = int(random()*1000)%10,int(random()*1000)%10
	print "[*] k0,k1 : %s,%s" % (k0,k1)
	diffcrypt = DiffCryptAnalysis([diff.sbox],[inputs,None])
	print "[*] calculating differentials...."
	diffcrypt.build_differentials()
	print "[*] finding pairs..."	
	print " (in,in) :=> (out,out) : differential data"
	for key in diffcrypt.differentials:
		in_diff,out_diff = key.split(" :=> ")
		in_diff = int(in_diff)
		out_diff = int(out_diff)
		#print in_diff,out_diff
		for i in inputs:
			i0 = diff._encrypt(i^in_diff,k0,k1)
			i1 = diff._encrypt(i,k0,k1)
			if i0^i1 == int(out_diff):
				print "[!] (%s,%s) => (%s, %s) : %s : %s" % (i,i^in_diff,i0,i1,key,diffcrypt.differentials[key])
			#else:
			#	print "[x] (%s,%s) => (%s, %s) : %s : %s" % (i,i^in_diff,i0,i1,key,diffcrypt.differentials[key])
	#diff_pairs = diffcrypt.getPairDifferentials()
	#for key in diff_pairs:
	#	if diffcrypt.differentials.has_key(key):
	#		print "*","[%s] %s <%s>" % (key,diff_pairs[key],diffcrypt.differentials[key][0])