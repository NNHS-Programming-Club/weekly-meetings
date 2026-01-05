import random

guess_pos = 0
start_pos = random.randint(1,5)

mouse_pos = start_pos
dis_check = mouse_pos - guess_pos


for T in range(100):
    guess_pos = int(input("guess where is the mouse. input the number\n"))
    

    # check if found or not
    if guess_pos == mouse_pos:
        print("you found it")
        break
    else:
        print("keep try")

        if mouse_pos == 1:
            mouse_pos = 2
        elif mouse_pos == 5:
            mouse_pos = 4
        else:
            ran_num = random.choice([-1,1])
            mouse_pos += ran_num

