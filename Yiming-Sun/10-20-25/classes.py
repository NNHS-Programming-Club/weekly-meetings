class Node:
    value = 0
    next = None
    def __init__ (self, value):
        self.value = value

def makeLL(arr):
    head = Node(arr[0])
    previuos = head

    for i in range(1,len(arr)):
        newHead = Node(arr[i])
