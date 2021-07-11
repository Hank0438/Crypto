from Crypto.PublicKey import RSA
from _primefac import williams_pp1, modinv, pollard_pm1


## Crypto{One of these primes is very smooth.}

def main(method="p-1"):
    pub = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDVRqqCXPYd6Xdl9GT7/kiJrYvy
8lohddAsi28qwMXCe2cDWuwZKzdB3R9NEnUxsHqwEuuGJBwJwIFJnmnvWurHjcYj
DUddp+4X8C9jtvCaLTgd+baSjo2eB0f+uiSL/9/4nN+vR3FliRm2mByeFCjppTQl
yioxCqbXYIMxGO4NcQIDAQAB
-----END PUBLIC KEY-----
"""
    pub = RSA.importKey(pub)
    print(pub.e, pub.n)
    if (method == "p+1"):
        p = williams_pp1(pub.n)
        q = pub.n // p
        print(p,q)
        assert pub.n == p * q
        priv = RSA.construct((pub.n, pub.e, modinv(pub.e, (p - 1) * (q - 1))))

    elif (method == "p-1"):
        p = pollard_pm1(pub.n)
        q = pub.n // p
        print(p,q)
        assert pub.n == p * q
        priv = RSA.construct((pub.n, pub.e, modinv(pub.e, (p - 1) * (q - 1))))

    with open('private_key.pem','wb') as f:
        f.write(priv.exportKey('PEM'))



# def pollard_pm1(N,prange=10000000):
#     """    
#     For one of N's prime p, 
#         1. If (p-1) is a K-smooth number. (k is small)
#         2. When all factor are appear in b
#     Then it can be solved by Pollard_P-1.
#     """
#     if isPrime(N):
#         return N
#     test_p = iter(get_primes(prange))
#     a = 2
#     while True:
#         try :
#             b = next(test_p)
#             a = pow(a, b, N)
#             p = gcd(a - 1, N)
#             if 1 < p < N:
#                 return p
#         except :
#             print("Pollard P-1 Failed.")
#             return 0


    


main("p+1")