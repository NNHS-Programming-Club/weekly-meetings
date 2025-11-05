class Node:
    value = 0
    next = None
    def __init__(self,value):
        self.value = value
    
head = Node(3)

def makeLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
       curr = Node(arr[i])
       prev.next = curr
       prev = curr

    return head

def printLL(head):
    cur = head
    while (cur != None):
        print(cur.value)
        cur = cur.next


head = makeLL([1, 2, 3, 4, 5,6,7,8])
printLL(head)










