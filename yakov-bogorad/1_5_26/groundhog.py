import random
from time import sleep

# groundhog simulation runs vars
catchinglist=[]
runs=1

while runs <= 100000:
    foundlist = [4,3,2,4,3,2]
    # groundhog init pos
    ghp = random.randint(1,5)
    caught = False
    looptime = 1
    for found in foundlist:
        if ghp == 1:
            ghp = ghp + 1
        elif ghp == 5:
            ghp = ghp - 1
        else:
            ghp = ghp + random.choice([-1,1])
        if found == ghp:
            caught = True
            #print(f"caught={caught}")
            catchinglist.append("True")
            break
    
        looptime= looptime + 1
        if looptime >= len(foundlist):
            caught = False
            #print(f"caught={caught}")
            catchinglist.append("False")
            break
    runs = runs + 1

ghtrues=0
ghfalses=0
for catch in catchinglist:
    if catch == "True":
        ghtrues = ghtrues + 1
    elif catch == "False":
        ghfalses = ghfalses + 1
print(f"Groundhog caught: {ghtrues} times.")
print(f"Groundhog escaped: {ghfalses} times.")