import random

win = True
rounds = int(input("input your rounds\n"))
max_num = int(input("input your max number\n"))
min_num = int(input("input your min number\n"))
guess_num = random.randint(min_num, max_num)

while (win):
    answer = int(input("write your answer\n"))

    if rounds == 0:
        print("rounds over")
        win = False
   
    else:
        if answer == guess_num:
            print("you win!")
            win = False
        
        elif answer > guess_num:
            print("big")
        
        elif answer < guess_num:
            print("small")


    
