#!/usr/bin/python3.6
from  hashlib import sha1, sha256
from base64 import b64encode, b64decode

flag = open('/home/sha1_dead/flag', 'r').read()
#flag = open('./flag', 'r').read()

def main():
    print("Give me the collision pair of SHA1")
    file1 = input("[>] :")
    file2 = input("[>] :")

    try:
        file1 = b64decode(file1.encode('ascii'))
        file2 = b64decode(file2.encode('ascii')) 
    except:
        print("Wrong format!")
        exit(1)
    if (file1 == b'') | (file2 == b'' ):
        print("Empty input!")
        exit(1)
    if (sha1(file1).hexdigest() == sha1(file2).hexdigest()):
        print(flag)
    else:
        print("SHA1 is alive!!!")
    exit(0)

main()