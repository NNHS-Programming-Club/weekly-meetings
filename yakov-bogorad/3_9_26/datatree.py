ligbist = []
truth = True
while truth == True:
    numberadd = int(input())
    ligbist.insert(0, numberadd)

    for i in range(len(ligbist)):
        if i == len(ligbist) - 1:
            break
        else:
            if ligbist[i] > ligbist[i+1]:
                ligbist[i], ligbist[i+1] = ligbist[i+1], ligbist[i]
    print(ligbist)