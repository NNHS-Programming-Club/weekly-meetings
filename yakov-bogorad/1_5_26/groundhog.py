import random
from time import sleep
# groundhog init pos
ghp = random.randint(1,5)
caught = False
looptime = 1

foundlist = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
for found in foundlist:
    if ghp == 1:
        ghp = ghp + 1
    elif ghp == 5:
        ghp = ghp - 1
    else:
        ghp = ghp + random.choice([-1,1])
    print(ghp)
    if found == ghp:
        caught = True
        print(f"caught={caught}")
    
    looptime= looptime + 1
    if looptime > 15:
        print(f"caught={caught}")