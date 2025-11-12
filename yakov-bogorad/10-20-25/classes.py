class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def makeLL(arr):
    head = Node(arr[0])
    previous = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])  # New node
        previous.next = new_node
        previous = new_node
    return head

def printLL(head):
    cur = head
    while cur is not None:
        print(cur.value)
        cur = cur.next

arr = [1,2,3,4,5]
head = makeLL(arr)
printLL(head)