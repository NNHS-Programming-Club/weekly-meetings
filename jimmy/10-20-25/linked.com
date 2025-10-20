class Node:
    value=0
    next = None
    def __init__ (self, value) :
        self.value = value


def makeLL (arr):
    head = Node(arr [0])    
    head2 = Node(2538234)

    head.next = head2