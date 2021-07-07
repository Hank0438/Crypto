import time
import sys


def long_to_bytes(data):
    data = str(hex(int(data)))[2:]
    return "".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])
    


def main():
    N = 64314292501050398570845898992815702729991685307749132803595907655074610196477
    e = 3
    c = 4167225289780248996551245469891565658388078429225395567331360886982151879073
    m = int.from_bytes(b"Your PIN code is \x00\x00\x00\x00", byteorder='big')
    P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = (m + x)^e - c
    roots = pol.small_roots(epsilon=1/30)
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()