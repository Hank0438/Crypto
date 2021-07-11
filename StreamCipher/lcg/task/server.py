#!/usr/bin/python3
import os
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

flag = open('./flag.txt', 'rb').read().strip()

class prng_lcg:
    m = bytes_to_long(os.urandom(40))  # the "multiplier"
    c = bytes_to_long(os.urandom(41))  # the "increment"
    n = getPrime(42*8)  # the "modulus"

    def __init__(self, seed):
        self.state = seed  # the "seed"

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state

def main():
    
    seed = bytes_to_long(os.urandom(32))
    gen = prng_lcg(seed)

    for i in range(10):
        rand = gen.next()
        print("Next: ", rand)

    rand = gen.next()
    print("Flag: ", bytes_to_long(flag)^rand) 
main()
