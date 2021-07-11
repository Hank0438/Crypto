import random
import os 
from Crypto.Util.number import long_to_bytes, bytes_to_long

flag = open('./flag.txt', 'rb').read().strip() 

random.seed(os.urandom(32))
f = open("./output.txt", "w")
for i in range(624):
    rand = random.getrandbits(32)
    f.write(f'Next: {rand}\n')

rand = random.getrandbits(len(flag)*8)
assert(long_to_bytes(bytes_to_long(flag)^rand^rand) == flag)
f.write(f'Flag: {bytes_to_long(flag)}\n') 