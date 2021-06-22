import random
import os 

random.seed(os.urandom(32))

random_sequence = []
for i in range(624):
    random_sequence.append(random.getrandbits(32))
print(random_sequence)