with open("raj-kasarle/11-17-25/input.txt") as inFile:
    inputList = inFile.readlines()
    inFile.close()

T = int(inputList[0])

line = 1

for case in range(T):
    N, M = map(int, inputList[line].split())
    a = []
    for i in range(N):
        a.append(list(map(int, inputList[line + i + 1].split())))
        
    for i in range(N):
        for j in range(M):
            print(a[i][j], end=", ")
        print()

    print()
    line += N + 1