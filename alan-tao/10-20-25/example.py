class Node:
    value = 0
    next = None
    def __init__(self, value):
        self.value = value


def makeLL(arr):
    head = Node(arr[0])
    previous = head

    for i in range(1, len(arr)):
        newHead = Node(arr[i]) #New node
        previous.next = newHead
        previous = newHead
    return head

def printLL(head):
    cur = head
    while (cur != None):
        print(cur.value)
        cur = cur.next

head = makeLL([5, 3, 5, 2, 3])
printLL(head)

