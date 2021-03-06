import random
import math
import sys
from math import log10
#105062213

monogram = {}
freqMono = ""
with open('./dict/monogram.txt') as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        monogram[line[0]] = line[1]
        freqMono += line[0]

with open('./' + sys.argv[1], 'r') as f:
    text = f.read()
cipher = ''
for x in text:
    if (ord(x) >= 65) & (ord(x) <= 90):
        cipher += chr(ord(x) + 32)
    else:
        cipher += x

cut = cipher.index('}')
secret = cipher[:cut+1]
cipher = cipher[cut+1:]
print("secret: ", secret)

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        with open(ngramfile) as f:
            for line in f.readlines():
                key,count = line.split(sep) 
                self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: 
                score += ngrams(text[i:i+self.L])
            else: 
                score += self.floor          
        return score

def genCiphertext(mappingTable, text):
    chipher = ""
    for x in text:
        chipher += mappingTable[x]
    return chipher

def genMappingTable():
    key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(key)
    mappingTable = {"{":"{", "}":"}", " ":" "}
    for i in range(26):
        mappingTable[chr(97+i)] = key[i]
    return mappingTable

def statAndInitMap(ciphertext):
    stat_dict = {}
    for i in ciphertext:
        if (i == "{") | (i == "}"):
            continue

        #if (ord(i) >= 97) & (ord(i) <= 122):
        #    i = chr(ord(i) - 32)
        
        if i not in list(stat_dict.keys()):
            stat_dict[i] = 1
        else:
            stat_dict[i] += 1

    stat_dict = sorted((value, key) for (key,value) in stat_dict.items())[::-1]
    #print(len(stat_dict))
    #print(stat_dict)
    initMap = {"{":"{", "}":"}"}
    for idx in range(26):
        initMap[stat_dict[idx][1]] = freqMono[idx]
        #initMap[chr(ord(stat_dict[idx][1])+32)] = freqMono[idx]
    return initMap

def splitCipher(ciphertext):
    words = []
    idx = 20
    while idx < len(ciphertext):
        x = ciphertext[idx]
        if (ord(x) >= 65) & (ord(x) <= 90):
            w = x
            idx += 1
            x = ciphertext[idx]
            while (ord(x) >= 97) & (ord(x) <= 122) & (idx < len(ciphertext)):
                w += x
                idx += 1
                if idx < len(ciphertext):
                    x = ciphertext[idx]
            words.append(w)
            print(w)
        idx += 1
    return words

#words = splitCipher(cipher)              
#print(words[:10])

# -- Stat frequency -- #
#initMap = statAndInitMap(cipher)
#print(initMap)



# -- Hill climbing -- #
bestMapping = {}
bestPlain = ''
bestScore = -99e9
fitness = ngram_score('./dict/trigram.txt')

for round in range(5):
    #currentMapping = statAndInitMap(cipher)
    currentMapping = genMappingTable() 
    currentPlain = genCiphertext(currentMapping, cipher)
    currentScore = fitness.score(currentPlain)
    iter = 0
    while iter < 1000:
    #for iter in range(3000):
        mapping = currentMapping.copy()
        idx2 = idx1 = random.randrange(26) + 97
        while idx2 == idx1:
            idx2 = random.randrange(26) + 97
        
        mapping[chr(idx1)], mapping[chr(idx2)] = mapping[chr(idx2)], mapping[chr(idx1)]
        plain = genCiphertext(mapping, cipher)
        score = fitness.score(plain)
        
        if score > currentScore:
            currentMapping = mapping
            currentPlain = plain
            currentScore = score
            print(f'[Round {round:1d} | Iter {iter:4d}] {currentScore:10.2f}:  {currentPlain[:60]}')
            iter = 0

        iter += 1
    if currentScore > bestScore:
        bestMapping = currentMapping
        bestPlain = currentPlain
        bestScore = currentScore
            
    print(f'plaintext:  {bestPlain[:100]}\n')
print(f'flag: {genCiphertext(bestMapping, secret)}\n')

'''
BWTTRGGDYARCLKEHW
cipher1: {BWTTRGGDYARCLKEHW}
cipher2: {BWTTRGGDYARCLKEHW}
cipher3: {BWTTRGGDYARCLKEHW}
cipher4: 
'''