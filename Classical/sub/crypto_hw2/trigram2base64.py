import base64

trigram_b64 = open('./dict/trigram_b64.txt', "a")

with open('./dict/trigram.txt') as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        trigram = line[0].encode("utf-8").lower()
        trigram = bytes.decode(base64.b64encode(trigram))
        trigram_b64.write(trigram + " " + line[1] + "\n")

trigram_b64.close()
        