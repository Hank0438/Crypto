import os
import random
from cracker import RandCrack

rc = RandCrack()

random.seed(os.urandom(32))
#random.seed(1)
num_list = []
for i in range(625):
    #rand = random.randrange(4294967295)
    rand = random.getrandbits(32)
    num_list.append(rand)

x0 = rc._to_int(rc._harden_inverse(rc._to_bitarray(num_list[0])))
x1 = rc._to_int(rc._harden_inverse(rc._to_bitarray(num_list[1])))
x397 = rc._to_int(rc._harden_inverse(rc._to_bitarray(num_list[397])))


guess0 = rc._to_int(rc._harden(rc._to_bitarray(rc.twist(x0, x1, x397))))
guess1 = rc._to_int(rc._harden(rc._to_bitarray(rc.twist(0x80000000, x1, x397))))
guess2 = rc._to_int(rc._harden(rc._to_bitarray(rc.twist(0x00000000, x1, x397))))
#rc.check_continuous(1, x0, x1)
print("guess0: ", guess0)
print("guess1: ", guess1)
print("guess2: ", guess2)
print("true x624: ", num_list[624])
#print(random.getrandbits(32))