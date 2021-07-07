from Crypto.Util.number import getPrime, isPrime, inverse 
import random



def main():
    FLAG = open("./flag.txt", "rb").read().strip()
    secret = random.randrange(1000, 9999)
    msg = f'Your PIN code is {secret}'
    print(msg)
    for _ in range(1000):
        p = getPrime(128)
        q = getPrime(128)
        if (p & 0x10000000000000000000000000000000) and (q & 0x10000000000000000000000000000000):
            break
    N = p*q
    e = 3
    c = pow(int.from_bytes(msg.encode(), byteorder='big'), e, N)
    print(f'N = {N}')
    print(f'e = {e}')
    print(f'c = {c}')

    try:
        res = int(input("[*] Verify the PIN code (4 numbers): "))
        if res == secret:
            print(f"[+] Here is the flag: {FLAG}")
        else:
            print("[x] Hacker sucks")
    except:
        print("[x] Somethings wrong QQ") 

main()

