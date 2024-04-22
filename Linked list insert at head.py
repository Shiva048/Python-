#LinkedLISTathead
class Node:
    def __init__(self,data):
         self.data=data 
         self.next = None
def printlinkedlist(head):
    curr = head
    while curr!= None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()

def insertAthead(head,ele):
    newBlock=Node(ele)
    if  head==None:
        return newBlock
    newBlock.next=head
    return newBlock

def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)

    if head == None:
        return newBlock

    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newBlock

    return head

l = [11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l :
    head = insertAthead(head, ele)

printlinkedlist(head)
