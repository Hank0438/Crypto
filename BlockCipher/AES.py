from Crypto.Cipher import AES

def unpad(pad_msg):
    unpad_msg = pad_msg[:-pad_msg[-1]]
    return unpad_msg

def encrypt(iv, text, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.encrypt(text)
    return text

def decrypt(iv, text, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.decrypt(text)
    return text

def main():
    key = b"0123456789abcdef"
    plaintext = b"flagflagflagflag"
    IV = b"STARWAR888888888"

    ciphertext = encrypt(IV, plaintext, key)
    print("ciphertext: %s" % ciphertext)

    plaintext_decrypted = decrypt(IV, ciphertext, key)
    print("plaintext: %s" % plaintext_decrypted)
    
if __name__ == '__main__':
    main()