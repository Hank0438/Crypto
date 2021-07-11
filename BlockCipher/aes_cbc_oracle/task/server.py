#!/usr/bin/python3
import binascii
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
import hashlib

flag = open("flag.txt", "rb").read().strip()
key = hashlib.md5(flag).hexdigest().encode()[:16]
IV = b"STARWAR888888888"


def pad(plain):
    # calculate padding length
    padding = 16 - len(plain) % 16

    # append the padding
    plain += bytes([padding] * padding)
    assert(len(plain) % 16 == 0)

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
    text = decrypt(iv, text)
    return text



def main():
    # print(b64encode(encrypt(IV, pad(flag))))
    assert(b64encode(encrypt(IV, pad(flag))) == b'tOe2unnhDCLBhU1oglSayChtYUjc6G4/SgDDGkpnJZg2Qfg+RRg8tVRxO2M2c+NVACfTsK3P3KoTlHBc5EwRbQ==')
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

if __name__ == '__main__':
    main()
