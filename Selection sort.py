def performSelectionSort(nums):
    n = len(nums)
    
    for fixThisIndex in range(n - 1, 0, -1):
        # some logic
        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 
 
        for index in range(fixThisIndex):
            # 0 1 2 3 4 
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]
        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp


 
 
n = int(input().strip())
nums = list(map(int, input().split()))
