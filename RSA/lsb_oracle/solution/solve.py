from pwn import *
from gmpy2 import *
from Crypto.Util.number import  getPrime, bytes_to_long, long_to_bytes



# p = getPrime(512)
# q = getPrime(512)
# n = p*q
# phi = (p-1)*(q-1)
# e = 65537
# d = invert(e,phi)    
# flag = b'FLAG{AAAAAAAAAAAAAAA123}'
# flag = int.from_bytes(flag, byteorder='big')
# c = pow(flag, e, n)
# print("m:",flag)

s = remote("127.0.0.1", 60007)

def oracle(c):
    s.recvuntil("input: ")
    s.sendline(str(c))
    s.recvuntil("output: ")
    return int(s.recvline().strip())

    # return pow(c, d, n) % 2

def recover_flag(n, e, c): 
    L = 0
    H = n
    t = pow(2, e, n)
    print(f"n-bits: {n.bit_length()}")
    for _ in range(n.bit_length()):
        c = (t * c) % n
        if oracle(c) == 0:
            H = (L + H) // 2
        else:
            L = (L + H) // 2
    m = L # plain text
    return m

def main():
    n = s.recvline().strip().split(b" ")[-1]
    n = int(n.decode())

    e = s.recvline().strip().split(b" ")[-1]
    e = int(e.decode())
    
    c = s.recvline().strip().split(b" ")[-1]
    c = int(c.decode())

    m = recover_flag(n, e, c)
    print("recover_flag: ", m)
    print(long_to_bytes(m))

    s.close()

main()