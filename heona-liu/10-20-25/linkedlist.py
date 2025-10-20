class Node:
    value = 0
    next = None

    def __init__(self, value):
        self.value = value


head = Node(3)

def makeLL(arr):
    head = Node(arr[0])
    previous = head
    for i in range(1, len(arr)):
        newHead = Node(arr[i])
        previous.next = newHead
        previous = newHead

def printLL(head):
    cur = head
    while (cur != cur):
        print(cur.value)
        cur = cur.next



        
lists = makeLL([1,2,3,4,5])
print(lists)




    #head.next = head2



# 
