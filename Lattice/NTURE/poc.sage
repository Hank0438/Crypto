N=7
p=3
q=41
Zx.<X> = ZZ[]
f= X^6 - X^4 + X^3 + X^2 - 1
g= X^6 + X^4 - X^2 - X
h= 19* X^6 + 38* X^5 + 6* X^4 + 32* X^3 + 24* X^2 + 37* X + 8
M = matrix(2*N)
for i in [0..N-1]: M[i,i] = 1
for i in [N..2*N-1]: M[i,i] = q
for i in [0..N-1]:
    for j in [0..N-1]:
        M[i+N,j] = ((Zx(GF(q)(1/p)*h)*X^i)%(X^N-1))[j]
pretty_print(M)
pretty_print(M.transpose().LLL())
pretty_print(f.coefficients(sparse=False))
pretty_print(g.coefficients(sparse=False))