import os
from Crypto.Util.number import bytes_to_long, GCD, inverse, getPrime
from functools import reduce

class prng_lcg:
    m = bytes_to_long(os.urandom(30))  # the "multiplier"
    c = bytes_to_long(os.urandom(31))  # the "increment"
    n = getPrime(32*8)  # the "modulus"

    def __init__(self, seed):
        self.state = seed  # the "seed"
        print("n=%d,\n m=%d,\n c=%d" % (self.n, self.m, self.c))

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(GCD, zeroes))
    return crack_unknown_multiplier(states, modulus)

def start():
    states = []  
    seed = bytes_to_long(os.urandom(32))
    gen = prng_lcg(seed)

    for i in range(10):
        rand = gen.next()
        #print("Next: ", rand)
        rand = input("Next: ")
        states.append(rand)
    try:
        modulus, multiplier, increment = crack_unknown_modulus(states)
        print("n=%d,\n m=%d,\n c=%d" % (modulus, multiplier, increment))
        num = (states[-1]*multiplier + increment) % modulus
        print(num)
        num = int(input("[>] Give me a number: "))
        if num == gen.next():
            print("Congratulation!!")
    except ValueError:
        print("Not integer!!")



start()