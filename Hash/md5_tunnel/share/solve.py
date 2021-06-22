import sys
import os
import hashlib


key = os.urandom(32)

m = hashlib.md5()
prefix = "Crypto is fun" + " "*51
prefix = prefix.encode('ascii')
m.update(prefix)
print("partial:", m.digest())

### ./par_md5 prefix ###
'''
Partial MD5 is C08603BE 3CE1AA68 4B43510F 4B432744
Final MD5 is C7AB12D9 C9692A59 C4FA067E 52DDA4A5
'''

### ./md5-tunneling 0xC08603BE 0x3CE1AA68 0x4B43510F 0x4B432744 ###

m0 = [
    0x31,0xA7,0x9A,0x89,0xBB,0xDB,0xFD,0x08,0x8C,0xB1,0x57,0x6D,0x0E,0x2D,0xB5,0xD4,
    0x6D,0x01,0x62,0x4C,0x33,0x1E,0xBC,0x3D,0xD9,0x08,0xBD,0x4A,0x3A,0x3E,0x25,0x0D,
    0x55,0x2D,0x35,0x05,0x02,0x7A,0x54,0xE2,0x67,0xBB,0xAA,0x7C,0x54,0x77,0x21,0x94,
    0xF6,0x88,0x29,0xCE,0xEC,0x28,0xAC,0xBC,0xC5,0x31,0xFD,0x5C,0x9E,0xFC,0xF5,0xD4,
    0xB9,0x29,0xD7,0x3B,0x33,0xA1,0x8C,0x27,0xE7,0xF8,0xDB,0xB8,0x2A,0xD4,0xCF,0xD3,
    0x99,0xF2,0x35,0xB5,0x8B,0xF6,0x7F,0xFC,0x16,0x9D,0xBD,0x26,0x4B,0xBD,0x00,0xBD,
    0x1D,0x10,0xFB,0x20,0x26,0x93,0xF3,0x66,0x66,0x03,0x25,0x6A,0x9D,0xFC,0x90,0xBD,
    0xFD,0x78,0x2D,0xF3,0x7C,0xA6,0xFB,0x20,0xA8,0x7F,0xC5,0xCB,0xAF,0x92,0x8D,0xD4
]

m1 = [
    0x31,0xA7,0x9A,0x89,0xBB,0xDB,0xFD,0x08,0x8C,0xB1,0x57,0x6D,0x0E,0x2D,0xB5,0xD4,
    0x6D,0x01,0x62,0xCC,0x33,0x1E,0xBC,0x3D,0xD9,0x08,0xBD,0x4A,0x3A,0x3E,0x25,0x0D,
    0x55,0x2D,0x35,0x05,0x02,0x7A,0x54,0xE2,0x67,0xBB,0xAA,0x7C,0x54,0xF7,0x21,0x94,
    0xF6,0x88,0x29,0xCE,0xEC,0x28,0xAC,0xBC,0xC5,0x31,0xFD,0xDC,0x9E,0xFC,0xF5,0xD4,
    0xB9,0x29,0xD7,0x3B,0x33,0xA1,0x8C,0x27,0xE7,0xF8,0xDB,0xB8,0x2A,0xD4,0xCF,0xD3,
    0x99,0xF2,0x35,0x35,0x8B,0xF6,0x7F,0xFC,0x16,0x9D,0xBD,0x26,0x4B,0xBD,0x00,0xBD,
    0x1D,0x10,0xFB,0x20,0x26,0x93,0xF3,0x66,0x66,0x03,0x25,0x6A,0x9D,0x7C,0x90,0xBD,
    0xFD,0x78,0x2D,0xF3,0x7C,0xA6,0xFB,0x20,0xA8,0x7F,0xC5,0x4B,0xAF,0x92,0x8D,0xD4
]
print(len(m1))

def trans(mess):
    st = ''
    for _ in mess:
        s = hex(_)[2:]
        st += s.rjust(2, '0')
    return st


'''
print(trans(m0)==trans(m1))
print(trans(m0))
print(len(trans(m1)))
'''
print('========= usr ========')
m0 = trans(m0)
m1 = trans(m1)
#print('m0_len: ', len(m0))
#print('m1_len: ', len(m1))
usr = '20' * 51 + m0
usr1 = '20' * 51 + m1
#print('usr_len: ', len(usr))
#print('usr1_len: ', len(usr1))





print('usr: ', usr)
print('usr1: ', usr1)
print('usr == usr1: ', usr == usr1)
usr = bytes.fromhex(usr)
usr1 = bytes.fromhex(usr1)

print('========= mac ========')

mac = hashlib.md5(b'Crypto is fun' + usr + key).digest()
mac1 = hashlib.md5(b'Crypto is fun' + usr1 + key).digest()
print('mac: ', mac)
print('mac1: ', mac1)
print('mac == mac1: ', mac == mac1)
