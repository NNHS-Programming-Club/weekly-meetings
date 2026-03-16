#truth = True
#while truth == True:
#treeInput = int(input())

class numClass:
    def __init__(self, val, cLeft, cRight):
        self.v = val
        self.l = cLeft
        self.r = cRight

rootVal = int(input("enter number: "))
root = numClass(rootVal, None, None)

def insert(val, cur):
    if (val <= cur.v):
        if cur.l == None and cur.r == None:
            insert(val, cur.l)
    else:
        if cur.l == None and cur.r == None:
            insert(val, cur.r)

insert(45, root)

#def search(val):
