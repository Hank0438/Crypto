#!/usr/bin/python3.7
import os
import random
import sys

# with open('/home/mt19937/flag') as f:
#     flag = f.read()
flag = "test\{test\}"

def start():
    random.seed(os.urandom(32))
    num_list = []
    for i in range(624):
        #rand = random.randrange(4294967295)
        rand = random.getrandbits(32)
        num_list.append(rand)
    
    try:
        print("Oh! Great one who summons me, I stand by my oath: loyalty to wishes 3 !")
        
        first = int(input("[>] Give me the first index: "))
        print("[>] Here is the first number: %d" % num_list[first])
        sys.stdout.flush()
        
        second = int(input("[>] Give me the second index: "))
        print("[>] Here is the second number: %d" % num_list[second])
        sys.stdout.flush()

        third = int(input("[>] Give me the third index: "))
        if num_list[third] < 1000000000:
            print("[>] Here is the third number: %d" % num_list[third])
        else:
            print("[>] Bad luck :( a genie without a master, goes back in their lamp.")       
        sys.stdout.flush()

        guess = int(input("[>] There is no wish for predict random: "))
        next = random.getrandbits(32)
        if guess == next:
            print("[>] As you wish, Master!! Here is flag")
            print(flag)
        else:
            print("[>] You seek glory for yourself. And you would win it off the backs of the people!")
        exit(0)
    except:
        print("[>] Couple thousand years in a Cave of Wonders ought to cool you off.")
        exit(1)

start()
