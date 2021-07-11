#!/usr/bin/env python3
import hashlib
from base64 import b64encode, b64decode

flag = open('/home/sha256_lea/flag', 'r').read()
#flag = open('./flag', 'r').read()

salt = open('/home/sha256_lea/salt', 'r').read().strip()
#salt = open('./salt', 'r').read().strip()
salt = salt.encode('ascii')
assert(len(salt) == 44)


def main():
    try:
        token = b64encode(b"user=someone")
        inside = salt + b64decode(token)
        auth = hashlib.sha256(inside).hexdigest()
        print("auht: ", auth)
        token2 = input("input your token: ").strip()
        inside2 = salt + b64decode(token2.encode('ascii'))
        auth2 = input("input your authentication code: ").strip()
        
        secret_auth = hashlib.sha256(inside2).hexdigest()

        if auth2 == secret_auth:
            if b"user=admin" in b64decode(token2):
                print(flag)
            else:
                print("YOU ARE NOT ADMIN, GO AWAY!")
        else:
            print("YOU ARE NOT ALLOW TO CHANGE MY TOKEN!")
    except:
        exit(0)

if __name__ == '__main__':
    main()


