import time
import sys


def long_to_bytes(data):
    data = str(hex(int(data)))[2:]
    return "".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])
    


def main():
    N = 51717432716920942894634052023520103985952343080811355937368413523723772369601
    e = 3
    c = 30011104490442414990008030858653560946902060401209553620837124755416304424963
    m = int.from_bytes(b"Your PIN code is \x00\x00\x00\x00", byteorder='big')
    P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = (m + x)^e - c
    roots = pol.small_roots(epsilon=1/30)
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()