import random

random_range = random.randrange(1,10)
n, m = map(int, input("size:\n").split())

def div_borad():
    for i in range(n):
        for k in range(m):
            print(random_range , end='')
        return print()


ball_num = []
ball_num = div_borad()

print(ball_num)

'''    
T = int(input())

for _ in range(T):
    
grid = []

    do_map = map(div_borad() ,ball_num)
    number_list = list(do_map)
'''