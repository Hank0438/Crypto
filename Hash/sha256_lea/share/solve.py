#!/usr/bin/env python3
import hashlib
from base64 import b64encode, b64decode

flag = open('./flag', 'r').read()

salt = open('./salt', 'r').read()
salt = salt.encode('ascii')
assert(len(salt) == 44)

'''
hashpump -s 8dad6cd30ea1682cf6d8864e53ab954127ecc88c52f12fc858f88e208af33506 -d user=someone -k 44 -a user=admin
'''
fake_token = b"user=someone\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0user=admin"
fake_auth = "a4968525c9f8ec6a02b8725bb87597aced97906189e987c1efd5e545d68d8c32"
print(b64encode(fake_token).decode('ascii'))
print(fake_auth)

def main():
    try:
        token = b64encode(b"user=someone")
        inside0 = salt + b64decode(token)
        auth = hashlib.sha256(inside0).hexdigest()
        print("inside0: ", inside0)

        print("your token:", token.decode('ascii'))
        print("your authentication code:", auth)

        #token = input("input your token: ").strip()
        token = b64encode(fake_token)
        #auth = input("input your authentication code: ").strip()
        auth = fake_auth
        #inside = salt + b64decode(token.encode('ascii'))
        inside = salt + b64decode(token)
        secret_auth = hashlib.sha256(inside).hexdigest()
        print("auth: ", auth)
        print("secret_auth: ", secret_auth)
        print("inside: ", inside)

        if auth == secret_auth:
            if b"user=admin" in b64decode(token):
                print(flag)
            else:
                print("YOU ARE NOT ADMIN, GO AWAY!")
        else:
            print("YOU ARE NOT ALLOW TO CHANGE MY TOKEN!")
    except:
        exit(0)

#main()


