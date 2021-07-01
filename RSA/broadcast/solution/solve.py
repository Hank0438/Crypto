from Crypto.Util.number import getPrime, isPrime, inverse 
import random
from functools import reduce
import gmpy2


# def main():
flag = b'Crypto{AAAAAAAAAAAaa}'
e = 3
m = int.from_bytes(flag, byteorder='big')
print(m)


n1 = getPrime(128)*getPrime(128)
c1 = pow(m,e,n1)

n2 = getPrime(128)*getPrime(128)
c2 = pow(m,e,n2)

n3 = getPrime(128)*getPrime(128)
c3 = pow(m,e,n3)

# m = 102
# n1 = 493
# n2 = 517
# n3 = 943
# e=3
# c1 = pow(m,e,n1)
# c2 = pow(m,e,n2)
# c3 = pow(m,e,n3)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda x, y: x*y, n)  # product all
 
    for ni, ai in zip(n, a):
        p = prod // ni
        sum += ai * inverse(p, ni) * p
    return sum % prod


common = chinese_remainder([n1,n2,n3], [c1,c2,c3])
decrypted_msg = int(gmpy2.iroot(common, e)[0])
print(decrypted_msg.to_bytes(0x20, byteorder='big').strip(b'\x00'))