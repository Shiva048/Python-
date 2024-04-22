class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def printlist(head):
    # below line of code is assigning head to curr variable
    curr=head
 
    # below line is checking whether curr reached none or not
    while curr!=None:
 
        # here we are trying to print data in curr pointer 
        print(curr.data,end=" ")
        curr=curr.next
    print()
 
 
# 1. Deleting head node in a linked list
# 2. Deleting node at specific position in linked list
 
# Before deletion
# 21 --> 45 --> 100 --> 12 --> 78 --> 56 --> None 
# 1       2      3       4      5      6 
 
# position = 4
 
# 9500 
# 5631 
 
def deleteHeadNodeInLinkedList(head):
    # delete link between first and second node
    # change the head to newHead
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
# After deletion
# 21 --> 45 --> 100 --> 78 --> 56 --> None 
# 1       2      3       4      5       
 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
    # curr --> points to (position - 1)
    mainNode = curr.next 
    # mainNode --> points to (position)
    nextNode = mainNode.next 
    # nextNode --> points to (position + 1)
    # 5630 --> None 
    # 5631 --> None 
    # 5632
    # 5630 --> 5632
    mainNode.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head
 
# 21 --> None 
# 45 --> 100 --> 12 
 
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)
 
head = deleteHeadNodeInLinkedList(head)
printlist(head)
