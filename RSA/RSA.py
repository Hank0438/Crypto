

def SquareAndMultiplyRecursive(x, y):
    if y == 0: 
        return 1
    k = SquareAndMultiply(x, y//2) ** 2
    return k * x if y % 2 else k

def SquareAndMultiply(x, n, k):
    x1 = 1
    x2 = x
    # k is bit length of n
    for i in range(k):
        if n&1 == 1:
            x1 = x1*x2
        x2 = x2**2
        n = n >> 1
    return x1


def SquareAndMultiplyByMontgomeryLadder(x, n, k):
    x1 = 1
    x2 = x
    # k is bit length of n
    for i in range(k):
        if n&1 == 1:
            x1 = x1*x2
            x2 = x2**2
        else:
            x2 = x1*x2
            x1 = x1**2
        n = n >> 1
    return x1

def gcd(a, b):
    pass
def pollard(n)
    a = 2
    b = 2
    while True:
        a = pow(a, b, n)
        d = gcd(a-1, n)
        if 1 < d < n: return d
        b += 1

import math
import gmpy2

def FermatFactorization(n):

    ceil = math.ceil
    sqrt = math.sqrt

    a = ceil(sqrt(n))
    b2 = a * a - n
    while not gmpy2.iroot(b2, 2)[1]:
        a = a + 1
        b2 = a * a - n
    b = sqrt(b2)
    return [a + b, a - b]

def williams_pp1(n):
    """    
    If (p+1) is a K-smooth number. (k is small)
    Then it can be solved by Pollard_P-1.
    """
    def mlucas(v, a, n):
        """ Helper function for williams_pp1().  Multiplies along a Lucas sequence modulo n. """
        v1, v2 = v, (v**2 - 2) % n
        for bit in bin(a)[3:]: v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n) if bit == "0" else ((v1*v2 - v) % n, (v2**2 - 2) % n)
        return v1
    
    if isprime(n): return n
    m = ispower(n)
    if m: return m
    for v in count(1):
        for p in primegen():
            e = ilog(isqrt(n), p)
            if e == 0: break
            for _ in range(e): v = mlucas(v, p, n)
            g = gcd(v - 2, n)
            if 1 < g < n: return g
            if g == n: break

SquareAndMultiplyByMontgomeryLadder(7, 0b10101, 5)
print(7**(0b10101))
print((0b10101))