input1 = input()
def goonkov(snord):
    if input1 == 1:
        return(1)
    return 2*(snord/2 +1 - goonkov(snord/2))