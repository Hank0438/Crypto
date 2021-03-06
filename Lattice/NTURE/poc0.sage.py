

# This file was *autogenerated* from the file poc0.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_7 = Integer(7); _sage_const_3 = Integer(3); _sage_const_41 = Integer(41); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_5 = Integer(5)
def cmap(t,p):
    if (ZZ(t)%p)>(p//_sage_const_2 ):
        return ((ZZ(t)%p)-p)
    else:
        return ZZ(t)%p

N=_sage_const_7 
p=_sage_const_3 
q=_sage_const_41 
print("(N,p,q)=",(N,p,q))
Zx = ZZ['X']; (X,) = Zx._first_ngens(1)
f=X**_sage_const_6 -X**_sage_const_4 +X**_sage_const_3 +X**_sage_const_2 -_sage_const_1 
g=X**_sage_const_6 +X**_sage_const_4 -X**_sage_const_2 -X
print("f=",f)
print("g=",g)
Pp = PolynomialRing(GF(p), names=('b',)); (b,) = Pp._first_ngens(1)
Pq = PolynomialRing(GF(q), names=('c',)); (c,) = Pq._first_ngens(1)
f3=Pp(f).inverse_mod(b**N-_sage_const_1 )
f41=Pq(f).inverse_mod(c**N-_sage_const_1 )
print("f_p=",f3(b=X))
print("f_q=",f41(c=X))
h=(p*f41*Pq(g))%(c**N-_sage_const_1 )
print("public key h: ",h(c=X))
r=X**_sage_const_6 -X**_sage_const_5 +X-_sage_const_1 
print("r=",r)
m=-X**_sage_const_5 +X**_sage_const_3 +X**_sage_const_2 -X+_sage_const_1 
print("message m:",m)
em=(Pq(r)*h)%(c**N-_sage_const_1 )+Pq(m)%(c**N-_sage_const_1 )
print("encrypted m: ", em(c=X))
A=(Pq(f)*em)%(c**N-_sage_const_1 )
print(A(c=X))
A1=[cmap(k,q) for k in A.list()]
print(Zx(A1))
print("decrypted message m: ", Zx([cmap(k,p) for k in Pp((Zx(A1)*Zx(f3))%(X**N-_sage_const_1 )).list()]))

