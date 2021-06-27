

# This file was *autogenerated* from the file ./solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_16 = Integer(16); _sage_const_0 = Integer(0); _sage_const_51717432716920942894634052023520103985952343080811355937368413523723772369601 = Integer(51717432716920942894634052023520103985952343080811355937368413523723772369601); _sage_const_3 = Integer(3); _sage_const_30011104490442414990008030858653560946902060401209553620837124755416304424963 = Integer(30011104490442414990008030858653560946902060401209553620837124755416304424963); _sage_const_1 = Integer(1); _sage_const_30 = Integer(30)
import time
import sys


def long_to_bytes(data):
    data = str(hex(int(data)))[_sage_const_2 :]
    return "".join([chr(int(data[i:i + _sage_const_2 ], _sage_const_16 )) for i in range(_sage_const_0 , len(data), _sage_const_2 )])
    


def main():
    N = _sage_const_51717432716920942894634052023520103985952343080811355937368413523723772369601 
    e = _sage_const_3 
    c = _sage_const_30011104490442414990008030858653560946902060401209553620837124755416304424963 
    m = int.from_bytes(b"Your PIN code is \x00\x00\x00\x00", byteorder='big')
    P = PolynomialRing(Zmod(N), implementation='NTL', names=('x',)); (x,) = P._first_ngens(1)
    pol = (m + x)**e - c
    roots = pol.small_roots(epsilon=_sage_const_1 /_sage_const_30 )
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()

