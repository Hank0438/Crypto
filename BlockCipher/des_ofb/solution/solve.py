from Crypto.Cipher import DES

search_arr = [('B', 13, 93), ('K', 14, 93), ('P', 15, 93), ('C', 0, 94), ('T', 1, 94), ('F', 2, 94), ('{', 3, 94), ('s', 4, 94), ('o', 5, 94), ('_', 6, 94), ('i', 7, 94), ('t', 8, 94), ('s', 9, 94), ('_', 10, 94), ('j', 11, 94), ('u', 12, 94), ('s', 13, 94), ('t', 14, 94), ('_', 15, 94), ('a', 0, 95), ('_', 1, 95), ('s', 2, 95), ('h', 3, 95), ('o', 4, 95), ('r', 5, 95), ('t', 6, 95), ('_', 7, 95), ('r', 8, 95), ('e', 9, 95), ('p', 10, 95), ('e', 11, 95), ('a', 12, 95), ('t', 13, 95), ('i', 14, 95), ('n', 15, 95), ('g', 0, 96), ('_', 1, 96), ('o', 2, 96), ('t', 3, 96), ('p', 4, 96), ('!', 5, 96), ('}', 6, 96), ('\n', 7, 96)]

ct2=open("ciphertext2","wb")
ct=open("ciphertext","rb").read()
pt=[]
best_arr = []
fix_counter = 0
target = b'BKPCTF'
patch = [19,0,9,1,25,9,]
for i in range(16):
    counts=[0]*256
    for c in ct[i::16]:
        counts[c]+=1
    mx=0
    best=0
    for k, val in enumerate(counts):
        if val>mx:
            mx=val
            best=k
    if i==6:
        best=0x53
    if i==13:
        best=0x16
    if i==15:
        best=0x18
    print("Key:", best)
    ptt=[]
    best_arr.append(best)
    for idx, c in enumerate(ct[i::16]):
        ptt.append(chr(c^best^ord(" ")))

        if fix_counter < 6:
            if (ptt[-1], len(pt), idx) in search_arr: 
                if bytes([ord(ptt[-1])]) in target:
                    print(ptt[-1])
                    ct = ct[:(i+(idx*16))] + bytes([c^patch[fix_counter]]) + ct[(i+(idx*16)+1):]
                    fix_counter += 1
        # else:
        #     ct2[i+(idx*16)] = bytes([c])
    # print("".join(ptt))
    pt.append("".join(ptt))

ct2.write(ct)
ct2.close()
fix_flag = []
res=[]
for i in range(len(pt[0])):
    for j in range(16):
        try:
            res.append(pt[j][i])
            if( i >= 93):
                if ((i==93) & (j<13)):
                    continue
                fix_flag.append((pt[j][i], j, i))
        except:
            pass

print(fix_flag)
print("".join(res))