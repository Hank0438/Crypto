from Crypto.Util.number import getPrime

def main():
    flag = open("./flag.txt", "rb").read().strip()
    m = int.from_bytes(flag, byteorder='big')
    q = getPrime(256)
    p1 = getPrime(256)
    p2 = getPrime(256)
    N1 = p1*q
    N2 = p2*q
    e = 65537
    c1 = pow(m, e, N1)
    c2 = pow(m, e, N2)


    f = open("output.txt", "w")
    f.write(f"e = {e}\n")
    f.write(f"N1 = {N1}\n")
    f.write(f"N2 = {N2}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"c2 = {c2}\n")

if __name__ == '__main__':
    main()
    
