def bitflip(a):

    s = b'role=guest&id=0001&admin=0' 
    a = bytes.fromhex(a)
    i = s.index(b'admin=0')+len(b'admin=')
    a = a[:i] + bytes([ a[i]^1 ]) + a[i+1:]

    print(a.hex())


# print(s.index(b'admin=0')+len(b'admin='))
a = "eca31517117b4fe0ed692a57772cf8ebe70a6c268512bb3c67a27d83b5c17b150fee1efb4c25cfd91055c3ae4e81988a"
bitflip(a)