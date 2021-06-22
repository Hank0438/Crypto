#!/usr/bin/python3.6
import requests
from  hashlib import sha1, sha256
from base64 import b64encode, b64decode

#flag = open('/home/sha1_dead/flag').read()
flag = open('./flag', 'r').read()

'''
pdf1 = open("shattered-1.pdf", "rb").read()
pdf2 = open("shattered-2.pdf", "rb").read()


print(sha1(pdf1).hexdigest())
print(sha1(pdf2).hexdigest())
print(sha256(pdf1).hexdigest())
print(sha256(pdf2).hexdigest())
print(len(pdf1))
print(len(pdf2))
'''

#file1 = open("upload1","w")
#file2 = open("upload2","w")
#file1.write(b64encode(pdf1).decode('ascii'))
#file2.write(b64encode(pdf2).decode('ascii'))

print("Give me the collision pair of SHA1")

file1 = open("upload1","r").read()
file2 = open("upload2","r").read()
#file1 = input("[>] :")
#file2 = input("[>] :")

try:
    file1 = b64decode(file1.encode('ascii'))
    file2 = b64decode(file2.encode('ascii')) 
except:
    print("Not base64!")
    exit(1)
if (file1 == b'') | (file2 == b'' ):
    print("Empty input!")
    exit(1)
if (sha1(file1).hexdigest() == sha1(file2).hexdigest()):
    print(flag)
else:
    print("SHA1 is alive!!!")
exit(0)
