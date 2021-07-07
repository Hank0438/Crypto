#!/usr/bin/python3.9
from Crypto.Util.number import *
from gmpy2 import *
import random
import sys,os


# sys.stdin  = os.fdopen(sys.stdin.fileno(), 'r', 0)
# sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
# rnd = SystemRandom()

def calcA(g,n,num):
    res = pow(g,num,n*n)
    r = random.randint(0,n-1)
    magic = pow(r,n,n*n)
    res = (res*magic)%(n*n)
    return res
    
def calcB(phi,n,u,num):
    res = pow(num,phi,n*n)
    res = (res - 1)//n
    res = (res*u)%n
    return res

if __name__ == '__main__':
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    phi = (p-1)*(q-1)
    g = n+1
    u = invert(phi,n)    
    flag = open("./flag.txt", "rb").read().strip()
    flag = int.from_bytes(flag, byteorder='big')

    print('Here is the flag!')
    print(calcA(g,n,flag))
    for i in range(2048):
        m = input('cmd: ')
        if m[0] == 'A':
            m = input('input: ')
            
            m = int(m)
            print(calcA(g,n,m))
        elif m[0] == 'B':
            m = input('input: ')
            try:
                m = int(m)
                print(calcB(phi,n,u,m) % 16)
            except:
                print('no')
                exit(0)