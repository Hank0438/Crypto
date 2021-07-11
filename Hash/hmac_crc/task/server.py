import hashlib

#!/usr/bin/env python
def to_bits(length, N):
  return [int(i) for i in bin(N)[2:].zfill(length)]

def from_bits(N):
  return int("".join(str(i) for i in N), 2)

CRC_POLY = to_bits(65, (2**64) + 0xeff67c77d13835f7)
CONST = to_bits(64, 0xabaddeadbeef1dea)

def crc(mesg):
  mesg += CONST
  shift = 0
  while shift < len(mesg) - 64:
    if mesg[shift]:
      for i in range(65):
        mesg[shift + i] ^= CRC_POLY[i]
    shift += 1
  return mesg[-64:]

INNER = to_bits(8, 0x36) * 8
OUTER = to_bits(8, 0x5c) * 8

def xor(x, y):
  return [g ^ h for (g, h) in zip(x, y)]

def hmac(h, key, mesg):
  return h(xor(key, OUTER) + h(xor(key, INNER) + mesg))

PLAIN_1 = "zupe zecret"

def str_to_bits(s):
  return [b for i in s for b in to_bits(8, ord(i))]

def bits_to_hex(b):
  return hex(from_bits(b)).rstrip("L")


def main():
  flag = open("./flag.txt", "r").read().strip()
  key = open("./key.txt", "rb").read().strip()
  assert(flag == ("Crypto{%s}" % hashlib.md5(key).hexdigest()))
  key = to_bits(64, int(key))

  print(PLAIN_1, "=>", bits_to_hex(hmac(crc, key, str_to_bits(PLAIN_1))))


main()