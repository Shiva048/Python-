#Searching in a Binary-Search
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
 
def printInorderTraversal(root):
    if root == None:
        return 
 
    printInorderTraversal(root.left)
    print(root.data, end = " ")
    printInorderTraversal(root.right)
n=int(input())
nums = list(map(int,input().split()))
target=int(input())
found=False
root = None 
for ele in nums:
    root = insertIntoBST(root, ele)
for i in range(n):
    if target==nums[i]:
        found=True
if found==True :
    print("Target element is found")
else:
    print("Target element is not found")
