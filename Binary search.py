nums=[12,2,22,45,7,7,885,33,3445,55,66,5]
nums=sorted(nums)
target=33
left=0
right=len(nums)-1
found = False
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
        
if found == True:
    print("found")
else:
    print("not found")
