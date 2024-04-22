
# 51 --> 52 --> 53 --> 54 --> 55 --> 56 --> 57 --> 58 --> 59 --> None
# None<--  <--     <--    <--    <--    <--    <--    <--    <--
 
#https://pastebin.com/xtKGpArE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    # left to right link 
    # 11 --> 22 --> 33 --> 44 --> None  
    # newBlock = 44  
    # tail = 33 
    tail.next = newBlock 
 
    # right to left link 
    newBlock.prev = tail 
    return head
 
 
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    # 11 --> 22 --> 33 --> None 
    # newBlock = 10
    # head = 11 
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
 
def insertAtSpecificPosition(head, val, position):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position - 1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
    # 11 --> 22 --> 33 --> 44 --> 55 --> 66 --> None 
    #  1      2     3       4      5      6 
 
    # (4, 12)
    # curr = 33 
    # newBlock = 12 
    # nextNode = 44 
 
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
 
    # 12 --> 44
    # 12 <-- 44 
 
    curr.next = newBlock 
    newBlock.prev = curr 
 
    # 33 --> 12 
    # 33 <-- 12 
 
    return head
 
 
 
 
 
 
 
 
 
 
 
 
 
l = [11, 22, 33, 44, 55, 66, 77]
head = None 
for ele in l:
    #head = addNodeAtTailOfLinkedList(head, ele)
    head = addNodeAtHeadOfLinkedList(head, ele)
 
printLeftToRightManner(head)
printRightToLeftManner(head)   
 
head = insertAtSpecificPosition(head, 12222, 3)
 
printLeftToRightManner(head)
printRightToLeftManner(head)        
# # object creation    
# obj1 = Node(121)
# obj2 = Node(145)
# obj3 = Node(678)
# obj4 = Node(89)
# obj5 = Node(12)
 
# # links establishments
# obj1.next = obj2 
# obj2.prev = obj1 
 
# obj2.next = obj3 
# obj3.prev = obj2 
 
# obj3.next = obj4 
# obj4.prev = obj3 
 
# obj4.next = obj5 
# obj5.prev = obj4 
 
# printLeftToRightManner(obj1)
# printRightToLeftManner(obj5)
 
