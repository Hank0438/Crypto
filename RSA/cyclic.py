from Crypto.Util.number import getPrime, isPrime, inverse 
import random

# y - ciphertext to reverse (i.e., RSA(x) = y)
# e and n - RSA public exponent and modulus
# returns the secret x
def cyclicEncryption(e, n, y):
    numSteps = 0
    prevEnc = y
    nextEnc = Encrypt(e, n, y)
    while nextEnc != y:
        prevEnc = nextEnc
        nextEnc = Encrypt(e, n, prevEnc)
        numSteps+=1
    return prevEnc, numSteps

# computes x power e (mod n)
def Encrypt(e, n, x):
    c = pow(x, e, n)
    print(f'c = {c}')
    return c

e = 7
p = getPrime(5)
q = getPrime(5)
N = p*q
flag = b'Crypto{cycling_attack_14_s0_C00L~~~~~~}'
m = int.from_bytes(flag, byteorder='big')
m = getPrime(9)
print(e, N, m)
input("@")
msg, times = cyclicEncryption(e, N, m)
print(msg, times)