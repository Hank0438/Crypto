def bitflip(a):

    a = bytes.fromhex(a)
    print(a)
    a = a[:6] + bytes([ a[6]^1 ]) + a[7:]
    print(a)

    print(a.hex())

a = "fe864cb8860a8faa6e25b981c404fa2ced656058dc5e806a7a3edd8fee84b42a"
bitflip(a)