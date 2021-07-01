import hashlib

class RsaPublicKey(object):
    def __init__(self, n, e):
        self.__dict__ = {'n':n, 'e':e}


def verify(message, signature, pub_key, blocksize=256):
    encrypted = int.from_bytes(signature, byteorder='big')
    decrypted = pow(encrypted, pub_key.e, pub_key.n)
    clearsig = decrypted.to_bytes(blocksize, byteorder='big')

    # If we can't find the signature  marker, verification failed.
    if clearsig[0:2] != b'\x00\x01':
        raise VerificationError('Verification failed')
    
    # Find the 00 separator between the padding and the payload
    try:
        sep_idx = clearsig.index(b'\x00', 2)
    except ValueError:
        raise VerificationError('Verification failed')
    
    # Get the hash and the hash method
    (method_name, signature_hash) = _find_method_hash(clearsig[sep_idx+1:])
    _hash = hashlib.new(method_name)
    _hash.update(message)
    message_hash = _hash.digest()


    
    # Compare the real hash to the hash in the signature
    if message_hash != signature_hash:
        raise VerificationError('Verification failed')

    return True

def _find_method_hash(method_hash):
    for (hashname, asn1code) in HASH_ASN1.items():
        if not method_hash.startswith(asn1code):
            continue
        
        return (hashname, method_hash[len(asn1code):])
    
    raise VerificationError('Verification failed')

HASH_ASN1 = {
    'md5': b'\x30\x20\x30\x0c\x06\x08\x2a\x86'
             b'\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
    'sha1': b'\x30\x21\x30\x09\x06\x05\x2b\x0e'
               b'\x03\x02\x1a\x05\x00\x04\x14',
    'sha256': b'\x30\x31\x30\x0d\x06\x09\x60\x86'
                 b'\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
    'sha384': b'\x30\x41\x30\x0d\x06\x09\x60\x86'
                 b'\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30',
    'sha512': b'\x30\x51\x30\x0d\x06\x09\x60\x86'
                 b'\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40',
}

flag = 'Crypto{I_think_U_R_master_of_rsa_signature!!!!!!!!}'
def main():
    print("Send me the cmd with rsa signature!")
    if verify(message, sig, key):
        if message == "HelloWorld":
            print("Hello World~")
        elif message == "CatFlag":
            print(flag)
        elif message == "BleichenbachersLowExponentAttack":
            print(flag)
    
    print("Hacker Bye~ Bye~")
    