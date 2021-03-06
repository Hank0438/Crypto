import binascii

# open the public key and strip the spaces so we have a decent array
fileKey = open("pubKey.txt", 'rb')
pubKey = fileKey.read().replace(b' ', b'').replace(b'L',b'').split(b',')
nbit = len(pubKey)
# open the encoded message
fileEnc = open("enc.txt", 'rb')
encoded = fileEnc.read().replace(b'L',b'')
print("start")
# create a large matrix of 0's (dimensions are public key length +1)
A = Matrix(ZZ,nbit+1,nbit+1)
# fill in the identity matrix
for i in range(nbit):
    A[i,i] = 1
# replace the bottom row with your public key
for i in range(nbit):
    A[i,nbit] = pubKey[i]
# last element is the encoded message
A[nbit,nbit] = -int(encoded)



res = A.LLL()
# resfil = open("res.txt", 'wb')
# resfil.write(res)

# print solution
# M = res.row(295).list()
# print(M)

for i in range(0, nbit + 1):
    # print solution
    M = res.row(i).list()
    flag = True
    for m in M:
        if m != 0 and m != 1:
            flag = False
            break
    if flag:
        print(i, M)
        M = ''.join(str(j) for j in M)
        # remove the last bit
        M = M[:-1]
        M = hex(int(M, 2))[2:]
        print(M)
        print(binascii.unhexlify(M))