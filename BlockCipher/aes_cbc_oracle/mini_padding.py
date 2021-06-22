#!/usr/bin/env python3
import binascii
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from pwn import *
'''
with open('/home/ctf/key', 'rb') as data:
    key = data.read().strip()

with open('/home/ctf/flag', 'rb') as data:
    flag = data.read().strip()
'''
key = b"0123456789abcdef"
flag = b"flagflagflagflag"

IV = b"STARWAR888888888"

def pad(plain):
    # calculate padding length
    padding = 16 - len(plain) % 16
    #print(padding)

    # append the padding
    plain += bytes([padding] * padding)
    assert(len(plain) % 16 == 0)

    #print(plain)
    return plain

def check(plain):
    # get the padding length
    length = plain[-1]
    if length > 16: return False

    return all(map(lambda x: x == length, plain[-length:]))

def encrypt(iv, text):
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.encrypt(text)
    return text

def decrypt(iv, text):
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.decrypt(text)
    return text

def in_message(message):
    iv, text = b64decode(message)[:16], b64decode(message)[16:]
    #print(iv)
    #print(text)
    text = decrypt(iv, text)
    return text

def main():
    '''
    assert(b64encode(encrypt(IV, pad(flag))) == b"XmmSv7+azqHCSPwBYfsVKVoqq+NpOaWrRHOYlLn3GlRAg4kdAVmEdc5L9koCHcxl5U0Ee28wMqTNdZYzd/BOaynUpmthknT0QdVGLXpx5Oko7QiK7+I0UVFhi8MP0+YFigbKhXMGzuv7ySqhnakeaRhaRGjRvVShMmjL0vitvuw=")
    cipher = b'^i\x92\xbf\xbf\x9a\xce\xa1\xc2H\xfc\x01a\xfb\x15)Z*\xab\xe3i9\xa5\xabDs\x98\x94\xb9\xf7\x1aT@\x83\x89\x1d\x01Y\x84u\xceK\xf6J\x02\x1d\xcce\xe5M\x04{o02\xa4\xcdu\x963w\xf0Nk)\xd4\xa6ka\x92t\xf4A\xd5F-zq\xe4\xe9(\xed\x08\x8a\xef\xe24QQa\x8b\xc3\x0f\xd3\xe6\x05\x8a\x06\xca\x85s\x06\xce\xeb\xfb\xc9*\xa1\x9d\xa9\x1ei\x18ZDh\xd1\xbdT\xa12h\xcb\xd2\xf8\xad\xbe\xec'
    '''
    while True:
        try:
            # get the cipher text
            inp = input("Give me something:")
            plain = in_message(inp)

            # check the padding
            if check(plain):
                print("YES, I will take that")
            else:
                print("NO, padding is invalid")

        except:
            exit(0)

def exploit():
    '''
    cipher = b64encode(encrypt(IV, pad(flag)))
    print(cipher)
    plain = in_message(cipher)
    print(plain)
    '''
    cipher_base64 = b'XmmSv7+azqHCSPwBYfsVKVoqq+NpOaWrRHOYlLn3GlRAg4kdAVmEdc5L9koCHcxl5U0Ee28wMqTNdZYzd/BOaynUpmthknT0QdVGLXpx5Oko7QiK7+I0UVFhi8MP0+YFigbKhXMGzuv7ySqhnakeaRhaRGjRvVShMmjL0vitvuw='
    cipher = b'^i\x92\xbf\xbf\x9a\xce\xa1\xc2H\xfc\x01a\xfb\x15)Z*\xab\xe3i9\xa5\xabDs\x98\x94\xb9\xf7\x1aT@\x83\x89\x1d\x01Y\x84u\xceK\xf6J\x02\x1d\xcce\xe5M\x04{o02\xa4\xcdu\x963w\xf0Nk)\xd4\xa6ka\x92t\xf4A\xd5F-zq\xe4\xe9(\xed\x08\x8a\xef\xe24QQa\x8b\xc3\x0f\xd3\xe6\x05\x8a\x06\xca\x85s\x06\xce\xeb\xfb\xc9*\xa1\x9d\xa9\x1ei\x18ZDh\xd1\xbdT\xa12h\xcb\xd2\xf8\xad\xbe\xec'
    '''
    b'^i\x92\xbf\xbf\x9a\xce\xa1\xc2H\xfc\x01a\xfb\x15)'
    b'Z*\xab\xe3i9\xa5\xabDs\x98\x94\xb9\xf7\x1aT'
    b'@\x83\x89\x1d\x01Y\x84u\xceK\xf6J\x02\x1d\xcce'
    b'\xe5M\x04{o02\xa4\xcdu\x963w\xf0Nk'
    b')\xd4\xa6ka\x92t\xf4A\xd5F-zq\xe4\xe9'
    b'(\xed\x08\x8a\xef\xe24QQa\x8b\xc3\x0f\xd3\xe6\x05'
    b'\x8a\x06\xca\x85s\x06\xce\xeb\xfb\xc9*\xa1\x9d\xa9\x1ei'
    b'\x18ZDh\xd1\xbdT\xa12h\xcb\xd2\xf8\xad\xbe\xec'
    '''
    #print(len(cipher)) #128=16*8
    
    r = remote('bamboofox.cs.nctu.edu.tw', 58792)
    first_block = 'BAMBOOFOX{XXXXXX'
    cipher_split = [cipher[b*16:(b+1)*16] for b in range(8)]
    plaintext = b''

    for block_no in range(4)[::-1]:
        evil_bytes = bytes([0])*16
        for block_size_idx in range(16)[::-1]:
            print('evil_bytes:', evil_bytes)
            for i in range(255):
                evil_bytes = evil_bytes[:block_size_idx] + bytes([i]) + evil_bytes[block_size_idx+1:]
                evil_cipher = cipher[:16*block_no] + evil_bytes + cipher[16*(block_no+1):16*(block_no+2)]
                cipher_base64 = b64encode(evil_cipher)
                r.sendlineafter('Give me something:', cipher_base64)
    
                if r.recvline()[:3] == b'YES':
                    print("YEAH!!!  ", bytes([i]))
                
                    cipher_split_byte = cipher_split[block_no][block_size_idx:block_size_idx+1]
                    padding = 16-block_size_idx
                    plainbyte = bytes([i^cipher_split_byte[0]^padding])
                    plaintext = plainbyte + plaintext
                    evil = bytes([plainbyte[0]^cipher_split_byte[0]^(padding+1)])
                    print(evil) 
                    #evil_bytes = evil_bytes[:block_size_idx] + evil + evil_bytes[block_size_idx+1:]
                
                    tmp_evil_bytes = evil_bytes[:block_size_idx] + evil
                    for k in range(15-block_size_idx):
                        tmp_evil_bytes += bytes([evil_bytes[block_size_idx+k+1] ^ padding ^ (padding+1)])
                
                    evil_bytes = b'' + tmp_evil_bytes
                
                    break
            print(plaintext)
    
    r.interactive()
    
if __name__ == '__main__':
    #main()
    #print(b'x'^b'\x01'^b'i')
    c1 = b'x'
    c0 = b'i'
    padd1 = b'\x01'
    p0 = c1[0]^c0[0]^padd1[0]
    print(p0)
    padd2 = b'\x02'
    c1 = p0^c0[0]^padd2[0]
    print(c1)

    c1 = b'\x0c'
    c0 = b'\x1e'
    padd1 = b'\x02'
    p0 = c1[0]^c0[0]^padd1[0]
    print(p0)
    padd2 = b'\x03'
    c1 = p0^c0[0]^padd2[0]
    print(c1)
    exploit()

#BAMBOOFOX{mAY_THE_Cbc_Be_WlTh_Y0U!!!}
