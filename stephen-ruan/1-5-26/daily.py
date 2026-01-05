import math
import random

guess = [2,2,4,4,2,2,4,4,2,2,4,4,2,2,4]
tests = 100000
caught = 0
catches = 0
for j in range (tests):
    mole = random.randint(1, 5)
    for i in range (len(guess)):
        if guess[i] == mole:
            caught = 1
        if mole == 1:
            mole += 1
        elif mole == 5:
            mole -= 1
        else:
            mole += random.choice([-1,1])
    if caught == 1:
        catches += 1
    caught = 0
print(str((catches/tests)*100)+"%")
    
