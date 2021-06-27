def cmap(t,p):
    if (ZZ(t)%p)>(p//2):
        return ((ZZ(t)%p)-p)
    else:
        return ZZ(t)%p

N=7
p=3
q=41
print("(N,p,q)=",(N,p,q))
Zx.<X> = ZZ[]
f=X^6-X^4+X^3+X^2-1
g=X^6+X^4-X^2-X
print("f=",f)
print("g=",g)
Pp.<b>=PolynomialRing(GF(p))
Pq.<c>=PolynomialRing(GF(q))
f3=Pp(f).inverse_mod(b^N-1)
f41=Pq(f).inverse_mod(c^N-1)
print("f_p=",f3(b=X))
print("f_q=",f41(c=X))
h=(p*f41*Pq(g))%(c^N-1)
print("public key h: ",h(c=X))
r=X^6-X^5+X-1
print("r=",r)
m=-X^5+X^3+X^2-X+1
print("message m:",m)
em=(Pq(r)*h)%(c^N-1)+Pq(m)%(c^N-1)
print("encrypted m: ", em(c=X))
A=(Pq(f)*em)%(c^N-1)
print(A(c=X))
A1=[cmap(k,q) for k in A.list()]
print(Zx(A1))
print("decrypted message m: ", Zx([cmap(k,p) for k in Pp((Zx(A1)*Zx(f3))%(X^N-1)).list()]))