import os
from Crypto.Util.number import getPrime, isPrime, inverse 

def next_prime(num):
    while True :
        num +=1
        if isPrime(num):
            return num

def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    if type(s) == str :
        return int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in s),16)
    if type(s) == bytes :
        return int.from_bytes(s,'big')

def main():
    try :
        print('Preparing your challenge ...')
        count = 0
        p,q,r = 0,0,0
        q = getPrime(1200)
        while True :
            count += 1
            r = getPrime(300)
            p = pow(r,4) + pow(r,3) + pow(r,2) + r + 1
            if isPrime(p) : 
                # print(r,p)
                break
        print('Ok!')

        e = getPrime(30)
        print(f'e = {str(e)}')
        n1 = r * next_prime(r)
        print('n1 : r * next_prime(r)')
        print(f'n1 = {str(n1)}')
        n2 = p * q
        print('n2 : p * q')
        print(f'n2 = {str(n2)}')

        FLAG = 'AIS3{S0me7im3s_I_h4tE_factorDB}'
        FLAG1 = s2n(FLAG[:len(FLAG)//2])
        FLAG2 = s2n(FLAG[len(FLAG)//2:])

        enc1 = pow(FLAG1, e, n1)
        enc2 = pow(FLAG2, e, n2)

        print('enc : pow(FLAG1, e, n1)')
        print(f'enc1 = {str(enc1)}')
        print('enc : pow(FLAG2, e, n2)')
        print(f'enc2 = {str(enc2)}')
        
        print('p,q,r are prime numbers.')
        print('((p-1) % r)**2 + ((r**5 - 1) % p)**2 == 0')
        print('Good luck !!')
    except:
        print('Something Wrong QAQ')

if __name__ == "__main__":
    main()
    