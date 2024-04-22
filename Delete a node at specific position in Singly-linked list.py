#Delete a node at specific position in Singly-linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head is None:
        return newBlock
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = newBlock
    return head

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
   
    mainNode = curr.next 
    nextNode = mainNode.next 
    mainNode.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head

n = int(input())
l = list(map(int, input().split()))
position = int(input())
head = None
for ele in l:
    head = insertAtEndOfTail(head, ele)
printlist(head)
head = deleteNodeAtSpecificPosition(head, position)
printlist(head)
