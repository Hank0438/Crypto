from hashlib import md5
import re
import base64

with open('./secret1.txt') as f:
    secret1 = f.read()
with open('./secret2.txt') as f:
    secret2 = f.read()
with open('./student.txt') as f:
    student = f.read()

def genToken(sid, secret):
    answer = sid + secret
    answer = md5(answer.encode("utf-8")).digest()
    answer = str(base64.b64encode(answer))
    answer = re.sub(r'\W+', '', answer)
    answer = re.sub(r'\d+', '', answer).upper()
    return answer

token1_table = open('./token1_table.txt', "a")
token2_table = open('./token2_table.txt', "a")        

with open('./student.txt') as f:
    student = f.readlines()

for sid in student:
    #sid = input("your student number:").strip()
    sid = sid.strip()
    print(sid)
    token1 = genToken(sid, secret1)
    token2 = genToken(sid, secret2)
    
    token1_table.write(token1+'\n')
    token2_table.write(token2+'\n')
    #print("token1: ", token1)
    #print("token2: ", token2)

token1_table.close()
token2_table.close()

