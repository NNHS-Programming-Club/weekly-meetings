class Node:
    value = 0
    next = None
    def __init__(self, value):
        self.value = value

def makeLinkedList(arr):
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        prev = cur
        cur = Node(arr[i])
        prev.next = cur
    return head

def printLL(head):
    cur = head
    while (cur != None):
        print(cur.value)
        cur = cur.next
    
    
head = makeLinkedList([213, 46123, 430, 12343, 24, 17, 458])
printLL(head)