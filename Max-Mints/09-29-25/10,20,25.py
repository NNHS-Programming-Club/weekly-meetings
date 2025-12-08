class Node:
    value = 0
    next = None

    def __init__ (self, value):
        self.value = value


numList = [1,2,3,4,5]

def makeLinkList(arr):
    head = Node(arr[0])
    previous = head

    for i in range(0, len(arr)):
        newHead = Node(arr[i])
        previous.next = newHead
        previous = newHead
        print(newHead.value)

def printLL(head):
    cur = head
    while cur != None:
        print(cur.value)
        
makeLinkList(numList)