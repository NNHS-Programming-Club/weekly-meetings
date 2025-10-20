class Node:
  value = 0
  next = None
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def construct(arr):
  head = Node(arr[0])
  cur = head
  for i in range(1, len(arr)):
    cur.next = Node(arr[i])
    cur = cur.next
  
  return head

def printLinkedList(head):
  cur = head
  while cur != None:
    print(cur.value, end=" -> ")
    cur = cur.next
  print()

def deleteKthElement(head, k):
  if (k == 0):
    return head.next
  
  cur = head
  for _ in range(k-1):
    cur = cur.next

  if (cur != None and cur.next != None):
    cur.next = cur.next.next  
  return head

def reverse(head):
  prev = None
  cur = head

  while (cur != None):
    newNext = cur.next
    cur.next = prev
    prev = cur
    cur = newNext
  
  return prev
  

head = construct([1, 2, 3, 4, 5])
printLinkedList(head)

head = deleteKthElement(head, 2)
printLinkedList(head)

head = reverse(head)
printLinkedList(head)