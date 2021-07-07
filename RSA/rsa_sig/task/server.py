
import hashlib
import rsa
import binascii
import os
from gmpy2 import mpz, iroot, powmod, mul, t_mod
from Crypto.Util.number import getPrime

# def to_bytes(n):
#     """ Return a bytes representation of a int """
#     return n.to_bytes((n.bit_length() // 8) + 1, byteorder='big')

# def from_bytes(b):
#     """ Makes a int from a bytestring """
#     return int.from_bytes(b, byteorder='big')

# def get_bit(n, b):
#     """ Returns the b-th rightmost bit of n """
#     return ((1 << b) & n) >> b

# def set_bit(n, b, x):
#     """ Returns n with the b-th rightmost bit set to x """
#     if x == 0: return ~(1 << b) & n
#     if x == 1: return (1 << b) | n

# def cube_root(n):
#     return int(iroot(mpz(n), 3)[0])



# message = "BleichenbachersLowExponentAttack".encode("ASCII")
# message_hash = hashlib.sha256(message).digest()


# ASN1_blob = rsa.HASH_ASN1['sha256']
# suffix = b'\x00' + ASN1_blob + message_hash

# print(binascii.hexlify(suffix))
# print(len(suffix))
# print(suffix[-1]&0x01 == 1) # easy suffix computation works only with odd target


# sig_suffix = 1
# for b in range(len(suffix)*8):
#     if get_bit(sig_suffix ** 3, b) != get_bit(from_bytes(suffix), b):
#         sig_suffix = set_bit(sig_suffix, b, 1)
# print(to_bytes(sig_suffix ** 3).endswith(suffix)) # BOOM
# print(len(to_bytes(sig_suffix ** 3)) * 8)
# while True:
#     prefix = b'\x00\x01' + os.urandom(2048//8 - 2)
#     sig_prefix = to_bytes(cube_root(from_bytes(prefix)))[:-len(suffix)] + b'\x00' * len(suffix)
#     sig = sig_prefix[:-len(suffix)] + to_bytes(sig_suffix)
#     if b'\x00' not in to_bytes(from_bytes(sig) ** 3)[:-len(suffix)]: break
# print(to_bytes(from_bytes(sig) ** 3).endswith(suffix))
# print(to_bytes(from_bytes(sig) ** 3).startswith(b'\x01'))
# print(len(to_bytes(from_bytes(sig) ** 3)) == 2048//8 - 1)
# print(b'\x00' not in to_bytes(from_bytes(sig) ** 3)[:-len(suffix)])
# print(binascii.hexlify(sig))
# print(binascii.hexlify(to_bytes(from_bytes(sig) ** 3)))


# p = getPrime(1024)
# q = getPrime(1024)
# N = p*q
# e = 3
# key = rsa.RsaPublicKey(N, e)
# print(rsa.verify(message, sig, key))
# print(f'sig: {sig}')
# sig = int.from_bytes(sig, byteorder='big')
# print(f'sig: {sig}')
# print(f'message: {message}')

def main():
    flag = open("./flag.txt", "rb").read().strip()
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    e = 3
    key = rsa.RsaPublicKey(N, e)

    print("[+] Public Key: ") 
    print(f"N = {N}")
    print(f"e = {e}")
    print("Send me the cmd with rsa signature!")
    sig = input("[*] sig (int type): ").strip()
    sig = int(sig).to_bytes(0x80, byteorder='big')
    message = input("[*] message (string type): ").strip()
    message = message.encode()
    try:
        if rsa.verify(message, sig, key):
            if message == b"BleichenbachersLowExponentAttack":
                print(flag)
            if message == b"HelloWorld":
                print("Hello World!")
        
        print("[-] Hacker 881")
    except:
        print("[-] Something wrong QQ")

main()