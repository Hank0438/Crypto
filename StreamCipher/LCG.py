#!/usr/bin/python3.7
import os
from Crypto.Util.number import bytes_to_long, GCD, inverse, getPrime
from functools import reduce
import sys

with open('/home/lcg/flag') as f:
    flag = f.read()

class LCG:
    def __init__(self, seed, param):
        self.state = seed  # the "seed"
        self.m = param[0]
        self.c = param[1]
        self.n = param[2]

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state

def start():

    m = 189153953815705994953679791362041557311480144903425708228438409203958970  # the "multiplier"
    c = 436739884908935959607136287328960222790271896378651819430740304248021842240  # the "increment"
    n = 95261208187898118531884929355668872111152375852661303536488694475425895511021  # the "modulus"
    
    seed = bytes_to_long(os.urandom(32))
    param = (m, c, n)
    gen = LCG(seed, param)

    for i in range(10):
        rand = gen.next()
        print("Next: ", rand)
    try:
        rand = gen.next()
        num = int(input("[>] Give me a number: "))
        if num == rand:
            print(flag)
        else:
            print("Oops!")
        exit(0)
    except ValueError:
        print("Not integer!!")
        exit(1)

start()