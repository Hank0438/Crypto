

# This file was *autogenerated* from the file ./solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_150 = Integer(150); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_42 = Integer(42)# sage 8.9

# Read ciphertext and public key from the 2 given files.
c = []
with open('ciphertext.txt', 'r') as f:
    data = f.read().strip(' ')
    c =  [int(num) for num in data.split(' ')]
c = vector(ZZ, c)

B = []
with open('key.pub', 'r') as f:
    for line in f.readlines():
        line = line.strip(' \n')
        B.append([int(num) for num in line.split(' ')])
B = matrix(ZZ, B)

# Nguyen's Attack.
n = _sage_const_150 
delta = _sage_const_3 
s = vector(ZZ, [delta]*n)
B6 = B.change_ring(Zmod(_sage_const_2 *delta))
left = (c + s).change_ring(Zmod(_sage_const_2 *delta))
m6 = (B6.solve_left(left)).change_ring(ZZ)
new_c = (c - m6*B) * _sage_const_2  / (_sage_const_2 *delta)

# embedded technique
new_B = (B*_sage_const_2 ).stack(new_c).augment(vector(ZZ, [_sage_const_0 ]*n + [_sage_const_1 ]))
new_B = new_B.change_ring(ZZ)

new_B_BKZ = new_B.BKZ()
shortest_vector = new_B_BKZ[_sage_const_0 ]
mbar = (B*_sage_const_2 ).solve_left(new_c - shortest_vector[:-_sage_const_1 ])
m = mbar * (_sage_const_2 *delta) + m6

print(''.join(map(chr, m[:_sage_const_42 ])))
