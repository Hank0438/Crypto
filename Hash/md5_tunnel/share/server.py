#!/usr/bin/python3 -u

import sys
import os
import hashlib

flag = open('/home/md5_tunnel/flag', 'r').read()
#flag = open('./flag', 'r').read()

def main():
    key = os.urandom(32)

    try:
        usr = input('[>] Username (hex): ')
        usr = bytes.fromhex(usr)
        mac = hashlib.md5(b'Crypto is fun' + usr + key).digest()
        print(f'[+] Mac: {mac.hex()}')
        
        usr2 = input('[>] Username (hex): ')
        mac2 = input('[>] Mac: ')
        usr2 = bytes.fromhex(usr2)
        mac2 = bytes.fromhex(mac2)
        mac2 = hashlib.md5(b'Crypto is fun' + usr2 + key).digest()
    
        if mac2 == mac:
            if usr2 != usr:
                print(f'[+] {flag}')
            else:
                print(f'[!] Try harder')
        else:
            print(f'[!] Invalid mac')
        exit(0)
    except:
        print("Wrong Input!")
        exit(1)
main()

