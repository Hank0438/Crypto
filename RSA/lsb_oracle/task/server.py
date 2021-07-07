#!/usr/bin/python3
from Crypto.Util.number import *
from gmpy2 import *



if __name__ == '__main__':
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    phi = (p-1)*(q-1)
    e = 65537
    d = invert(e,phi)    
    flag = open("/home/lsb_oracle/flag.txt", "rb").read().strip()
    flag = int.from_bytes(flag, byteorder='big')
    c = pow(flag, e, n)
    print(f'n = {n}')
    print(f'e = {e}')
    print(f'c = {c}')
    # m = pow(flag, d, n)
    # print(flag.to_bytes(0x20, byteorder='big'))
    
    for i in range(0x1000):
        try:
            m = int(input('input: ').strip())
            print("m: ", m)
            print(f'output: {pow(m, d, n) % 2}')
        except:
            print("something wrong QQ")

    print("Bye Bye~")