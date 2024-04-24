target=int(input())
n = int(input().strip())
num = list(map(int, input().split())) 
nums = sorted(num)

left = 0
right = len(nums) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        found = True
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("Target is present")
else:
    print("Target is not present")
