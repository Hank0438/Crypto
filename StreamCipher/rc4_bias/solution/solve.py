from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto import Random
import random
import hashlib 

MOD = 256


def KSA(key):
    ''' Key Scheduling Algorithm (from wikipedia):
        for i from 0 to 255
            S[i] := i
        endfor
        j := 0
        for i from 0 to 255
            j := (j + S[i] + key[i mod keylength]) mod 256
            swap values of S[i] and S[j]
        endfor
    '''
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    ''' Psudo Random Generation Algorithm (from wikipedia):
        i := 0
        j := 0
        while GeneratingOutput:
            i := (i + 1) mod 256
            j := (j + S[i]) mod 256
            swap values of S[i] and S[j]
            K := S[(S[i] + S[j]) mod 256]
            output K
        endwhile
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)

def encrypt(key, text):
    ''' :key -> encryption key used for encrypting, as hex string
        :text -> array of unicode values/ byte string to encrpyt/decrypt
    '''
    # For plaintext key, use this
    key = [c for c in key]
    keystream = get_keystream(key)

    res = []
    for c in text:
        val = bytes([c ^ next(keystream)])  # XOR and taking hex
        res.append(val)
    return b''.join(res)



def gen(stream=None, filename=None):
    if (stream==None) | (filename==None):
        print("Please give me stream type and output filename!")
        exit(-1)

    assert(encrypt(b"\x00"*0x100, encrypt(b"\x00"*0x100, b"\xab"*0x100)) == b"\xab"*0x100)
    # ### distinguish random or rc4
    stream_size = 0x100
    key_size = 0x10

    
    iterations = 20000
    
    f = open(filename, "w")

    for _ in range(iterations):

        if stream == "rc4":     
            # print("rc4 stream")
            key = Random.new().read(key_size)
            s = encrypt(key, b"\x00"*stream_size)
        else:
            # print("random stream")
            s = Random.new().read(stream_size)

        f.write(f'{str(bytes_to_long(s))}\n')

         

def distinguish(filename):
    dataset = open(filename, "r").readlines()
    arr = [0]*256
    for idx, data in enumerate(dataset):
        data = int(data.strip()).to_bytes(0x100, byteorder='big')
        for i in range(256):
            if data[i] == 0:
                arr[i] += 1

    # print(arr)
    if arr[1] > 130:
        return True
        
    return False



if __name__=='__main__':
    # rc4_list = [random.randint(0, 99) for _ in range(10) ]
    # for i in range(100):
    #     if i in rc4_list
    #         print(i)
    #         gen("rc4", "./stream_%d.txt" % i)   
    #     else:
    #         gen("random", "./output/stream_%d.txt" % i)
    



    # rc4_list = [2, 6, 18, 20, 37, 44, 76, 78, 88, 93]
    rc4_list = []
    for i in range(100):
        test = distinguish("../task/output/stream_%d.txt" % i)
        print(i, test)
        if test:
            rc4_list.append(i)


    ans = "".join([str(i) for i in rc4_list])
    ans = hashlib.md5(ans.encode()).hexdigest()
    print("Crypto{%s}" % ans)

