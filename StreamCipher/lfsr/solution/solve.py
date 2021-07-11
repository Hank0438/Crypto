def step1():
    barr = b''
    with open('keystream','rb') as f:
        data = f.read()
        i = 0
        while i < len(data):
            if data[i] == 194 or data[i] == 195:
                barr += bytes([ord(bytes([data[i], data[i+1]]).decode())])
                i += 1
            else:
                barr += bytes([ord(bytes([data[i]]).decode())])
            i += 1
    with open('decoded-keystream', 'wb') as f:
        f.write(barr)


def step2():
    outputs = []
    with open("decoded-keystream", "rb") as f:
        data = f.read()
        for b in data:
            arr = []
            tmp = b
            for i in range(8):
                arr += [tmp]
                tmp //= 2
            tmp = 0
            for l in arr[::-1]:
                outputs += [l - (tmp * 2)]
                tmp = l
    print(len(outputs))

    with open('proof', 'wb') as f:
        o = 0
        for i in range(8192):
            b = 0
            for j in range(8):
                b = (b<<1) + outputs[o]
                o += 1
            f.write(chr(b).encode())

from z3 import *

class lfsr():
    def __init__(self, init, mask, length):
        self.init = init
        self.mask = mask
        self.lengthmask = 2**(length+1)-1
        self.length = length

    def next(self):
        nextdata = (self.init << 1) & self.lengthmask
        i = self.init & self.mask & self.lengthmask

        output = 0
        for j in range(self.length):
            output ^= (i & 1)
            i = i >> 1

        nextdata ^= output
        self.init = nextdata
        return output

def combine(x1,x2,x3):
    return (x1*x2)^(x2*x3)^(x1*x3)

init1 = BitVec('init1', 48)
init2 = BitVec('init2', 48)
init3 = BitVec('init3', 48)

l1 = lfsr(init1, 0b100000000000000000000000010000000000000000000000, 48)
l2 = lfsr(init2, 0b100000000000000000000000000000000010000000000000, 48)
l3 = lfsr(init3, 0b100000100000000000000000000000000000000000000000, 48)

s = Solver()
with open('decoded-keystream', 'rb') as f:
    keystream = f.read()

outputs = []
for b in keystream:
    arr = []
    tmp = b
    for i in range(8):
        arr += [tmp]
        tmp //= 2

    tmp = 0
    for l in arr[::-1]:
        outputs += [l - (tmp * 2)]
        tmp = l

bits = 48*8
for i in range(bits):
    s.add(outputs[i] == combine(l1.next(), l2.next(), l3.next()))
    print(i)

s.check()
print(s.model())

def restore_flag():
    from Crypto.Util.number import long_to_bytes
    from hashlib import sha256

    flag = 'Crypto{' + sha256(long_to_bytes(70989122156399) + long_to_bytes(181037482648735) + long_to_bytes(191532558614761)).hexdigest() + '}'

    print(flag)

restore_flag()