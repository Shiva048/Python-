def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " is inserted into Q")
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return 
    ele = Q.pop(0)
    print("Deleted element is", ele)
 
def printQueue(Q):
    if len(Q) == 0:
        print("Nothing is present in Q")
        return 
    print(Q)
 
 
Q = []
printQueue(Q)
# []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
enQueue(Q, 50)
enQueue(Q, 60)
 
printQueue(Q)
# [10, 20, 30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [20, 30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [40, 50, 60]
 
 
deQueue(Q)
printQueue(Q)
# [50, 60]
 
 
deQueue(Q)
printQueue(Q)
 
# [60]
 
deQueue(Q)
printQueue(Q)
 
deQueue(Q)
printQueue(Q)
 
deQueue(Q)
printQueue(Q)
