import hashlib
import re

def main():
    pattern = r"[a-z0-9]{6}"
    ans = open("./ans.txt", "rb").read().split(b"\n")
    h = open("./hash.txt", "r").read().split("\n")
    for i in range(5):
        assert(re.fullmatch(pattern, ans[i].decode()) != None)
        assert(hashlib.md5(ans[i]).hexdigest() == h[i])

    print("Here is your flag: Crypto{%s}" % (b"".join(ans).decode()))

main()