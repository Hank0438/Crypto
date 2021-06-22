import sys
import os
import hashlib
import random

# with open('../flag.txt', 'rb') as f:
#     flag = f.read()
flag = b'Balsn{T0_4cCept_0r_tO_r3jeCt__7hat_1s_tHe_Qu3sT1On}'

version = sys.version.replace('\n', ' ')
print(f'Python {version}')
random.seed(os.urandom(1337))


for i in range(0x1337):
    print(random.randrange(3133731337))


# Encrypt flag
sha512 = hashlib.sha512()
for _ in range(1000):
    rnd = random.getrandbits(32)
    sha512.update(str(rnd).encode('ascii'))

key = sha512.digest()



enc = bytes(a ^ b for a, b in zip(flag, key))
print('Encrypted:', enc.hex())