import random
secret =random.randint(1,10)

question = int(input("Guess my number"))
while True :
   
    if question == secret:
        print("You did it")
        break
    else:
        print("Try again")
        question = int(input("Guess my number"))

