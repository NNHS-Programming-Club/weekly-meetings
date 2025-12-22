f = open("raj-kasarle/advent-of-code-2025/12-01-25/testcase.txt")

dialNum = 50
pointCases = 0
clickCases = 0

def dialTurn(dial, turnDirection, turnNumber):
    if turnDirection == 'L':
        return dial - turnNumber
    elif turnDirection == 'R':
        return dial + turnNumber

for i in f:
    direction = i[:1]
    turnNum = int(i[1:])
    newDialNum = dialTurn(dialNum, direction, turnNum)

    print(str(dialNum) + " becomes " + str(newDialNum) + " => " + str(newDialNum%100) + ", going " + direction + " " + str(turnNum) + " so it clicks " + str(abs((newDialNum - 1) // 100)) + " times")

    if newDialNum % 100 == 0:
        pointCases += 1
    
    clickCases += abs((newDialNum - 1) // 100)

    dialNum = newDialNum % 100

print(pointCases)
print(clickCases)