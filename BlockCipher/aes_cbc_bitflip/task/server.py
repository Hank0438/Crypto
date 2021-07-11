from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import binascii


key = get_random_bytes(16)
iv = get_random_bytes(16)

flag = open('flag.txt','r').read().strip()

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(pad(data,16,style='pkcs7'))
    return enc.hex()

def decrypt_data(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt(bytes.fromhex(encryptedParams))
    return unpad(paddedParams,16,style='pkcs7')

msg = b'role=guest&id=0001&admin=0'
print("Current Auth Message is : " + msg.decode())
print("Encryption of auth Message in hex : " + iv.hex() + encrypt_data(msg))
enc_msg = input("Give me Encrypted msg in hex : ")

final_dec_msg = decrypt_data(enc_msg)
try:
    if b"admin=1" in final_dec_msg:
        print('You got it!!')
        print(flag)
    else:
        print('Try again!!')
        exit()
except:
    print('Bye Bye!!')