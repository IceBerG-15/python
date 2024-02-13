def searchRange(nums, target):
    n = len(nums)-1
    left = 0
    right = n
    # ans = [-1,-1]
    mid = -1
    c=False
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1


nums = [5,7,7,8,8,10]
target = 8

a = searchRange(nums,target)
b = searchRange(nums[::-1],target)
print(a,len(nums)-b)