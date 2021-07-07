from Crypto.Util.number import getPrime

def main():
    flag = open("./flag.txt", "rb").read().strip()
    m = int.from_bytes(flag, byteorder='big')
    p = getPrime(256)
    q = getPrime(256)
    N = p*q
    e1 = getPrime(10)
    e2 = getPrime(10)
    c1 = pow(m, e1, N) 
    c2 = pow(m, e2, N)
    

    f = open("output.txt", "w")
    f.write(f"N = {N}\n")
    f.write(f"e1 = {e1}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"e2 = {e2}\n")
    f.write(f"c2 = {c2}\n")

if __name__ == '__main__':
    main()
    
