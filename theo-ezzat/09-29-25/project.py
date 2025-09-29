import random
secret =random.randint(1,10)
guess = 0
question = int(input("Guess my number"))
while guess != secret :
   
    if question == secret:
        print("You did it")
        break
    else:

