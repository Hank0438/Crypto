

# This file was *autogenerated* from the file ./poc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_7 = Integer(7); _sage_const_3 = Integer(3); _sage_const_41 = Integer(41); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_19 = Integer(19); _sage_const_38 = Integer(38); _sage_const_5 = Integer(5); _sage_const_32 = Integer(32); _sage_const_24 = Integer(24); _sage_const_37 = Integer(37); _sage_const_8 = Integer(8); _sage_const_0 = Integer(0)
N=_sage_const_7 
p=_sage_const_3 
q=_sage_const_41 
Zx = ZZ['X']; (X,) = Zx._first_ngens(1)
f=X**_sage_const_6 -X**_sage_const_4 +X**_sage_const_3 +X**_sage_const_2 -_sage_const_1 
g=X**_sage_const_6 +X**_sage_const_4 -X**_sage_const_2 -X
h=_sage_const_19 *X**_sage_const_6  + _sage_const_38 *X**_sage_const_5  + _sage_const_6 *X**_sage_const_4  + _sage_const_32 *X**_sage_const_3  + _sage_const_24 *X**_sage_const_2  + _sage_const_37 *X + _sage_const_8 
M = matrix(_sage_const_2 *N)
for i in (ellipsis_range(_sage_const_0 ,Ellipsis,N-_sage_const_1 )): M[i,i] = _sage_const_1 
for i in (ellipsis_range(N,Ellipsis,_sage_const_2 *N-_sage_const_1 )): M[i,i] = q
for i in (ellipsis_range(_sage_const_0 ,Ellipsis,N-_sage_const_1 )):
    for j in (ellipsis_range(_sage_const_0 ,Ellipsis,N-_sage_const_1 )):
        M[i+N,j] = ((Zx(GF(q)(_sage_const_1 /p)*h)*X**i)%(X**N-_sage_const_1 ))[j]
pretty_print(M)
pretty_print(M.transpose().LLL())
pretty_print(f.coefficients(sparse=False))
pretty_print(g.coefficients(sparse=False))
