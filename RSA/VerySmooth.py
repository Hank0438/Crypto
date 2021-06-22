from math import gcd

modulus = 'D546AA825CF61DE97765F464FBFE4889AD8BF2F25A2175D02C8B6F2AC0C5C27B67035AEC192B3741DD1F4D127531B07AB012EB86241C09C081499E69EF5AEAC78DC6230D475DA7EE17F02F63B6F09A2D381DF9B6928E8D9E0747FEBA248BFFDFF89CDFAF4771658919B6981C9E1428E9A53425CA2A310AA6D760833118EE0D71'
N = int(modulus, 16)
seed = 2  # seedは通常2か3, うまく分解できなかったときに動かす
B = 100000 # B-smoothと仮定する 通常100000まで

a = seed
G = 1
cnt = 0
M = 1
while(G<=1):
    M = M + 1
    if M >= B:
        break
    if M % 10000 == 0:
        print("M=" + str(M))
    a = pow(a, M, N)
    G = gcd(a-1, N)
if G > 1 and G < N:
    print("factor is " + str(G) + ", M = " + str(M))
else:
    print("try new seed")

print("p: " + str(G))
print("q: " + str(N//G))