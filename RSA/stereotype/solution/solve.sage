import time
import sys


def long_to_bytes(data):
    data = str(hex(int(data)))[2:]
    return "".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])
    


def main():
    N = 60259696438802824739601125817242188146078891917629227205809157440421934320057
    e = 3
    c = 54628725427538455885247976318697353582883460531963823959596505967156861036432
    m = int.from_bytes(b"Your PIN code is \x00\x00\x00\x00", byteorder='big')
    P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = (m + x)^e - c
    roots = pol.small_roots(epsilon=1/30)
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()