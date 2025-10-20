class Node:
    value = 0
    next = None
    def __init__(self, value):
        self.value = value

def makeLL(arr):
    head = Node(arr[0])
    previous = head

    for i in range(1, len(arr)):
        newHead = Node(arr[i])
        previous.next =newHead
        previous = newHead
        return newHead

def printLL(head):
    cur = head 