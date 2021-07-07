from Crypto.Util.number import getPrime, isPrime, inverse 
import random
from functools import reduce
import gmpy2


def main():
    flag = open("./flag.txt", "rb").read().strip()
    e = 3
    m = int.from_bytes(flag, byteorder='big')

    N1 = getPrime(200)*getPrime(200)
    N2 = getPrime(200)*getPrime(200)
    N3 = getPrime(200)*getPrime(200)
    c1 = pow(m,e,N1)
    c2 = pow(m,e,N2)
    c3 = pow(m,e,N3)

    f = open("output.txt", "w")
    f.write(f"N1 = {N1}\n")
    f.write(f"N2 = {N2}\n")
    f.write(f"N3 = {N3}\n")
    f.write(f"e = {e}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"c2 = {c2}\n")
    f.write(f"c3 = {c3}\n")

if __name__ == '__main__':
    main()
    

