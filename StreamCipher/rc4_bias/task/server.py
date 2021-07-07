from Crypto.Cipher import ARC4
from Crypto import Random


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



def distinguish_rc4(lines):
    max = 0
    sums = []
    for start in range(0, 31, 2):
        zeroes = 0
        for line in lines:
            # Get the second byte
            char = line.strip()[start:start+2]
            if char == "00":
                zeroes += 1

        sums.append(zeroes)
        if(zeroes > max):
            max = zeroes

    print()
    print("Average number of zeroes:")
    for sum in sums:
        print(sum / len(lines))

    # If the max was at index 1, we assume it is RC4
    rc4 = sums.index(max) == 1
    if rc4:
        return "rc4"
    else:
        return "aes"

def main():
    # assert(encrypt('Key', 'Plaintext')) == 'BBF316E8D940AF0AD3'
    # assert(encrypt('Key', 'BBF316E8D940AF0AD3')) == 'Plaintext'
    assert(encrypt(b"\x00"*0x100, encrypt(b"\x00"*0x100, b"\xab"*0x100)) == b"\xab"*0x100)
    # ### distinguish random or rc4
    stream_size = 0x100
    key_size = 0x10

    arr1 = [0]*key_size
    arr2 = [0]*key_size
    
    iterations = 100000

    for _ in range(iterations):
        stream1 = Random.new().read(stream_size)
        key = Random.new().read(key_size)
        stream2 = encrypt(key, b"\x00"*stream_size)
        for i in range(stream_size//key_size):
            for j in range(key_size):
                if stream1[i*key_size+j] == 0:
                    arr1[j] += 1
                if stream2[i*key_size+j] == 0:
                    arr2[j] += 1

    print(arr1[1]/(stream_size//key_size))
    print(arr2[1]/(stream_size//key_size))

    print(arr1)        
    print(arr2)        




if __name__=='__main__':
		main()
