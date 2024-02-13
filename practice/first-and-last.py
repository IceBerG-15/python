def searchRange(nums, target):
    if len(nums)==1:
        if target==nums[0]:
            return [0,0]
        return [-1,-1]
    n = len(nums)-1
    left = 0
    right = n
    ans = [-1,-1]
    mid = -1
    c = False
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            c = True
            break
        elif target<nums[mid]:
            right = mid-1
        else:
            left = mid+1
    # searching for first and last positions
    if c:
        left = mid
        right = mid
        if left>=0 and right+1<=n and nums[right+1]==target:
            while nums[right+1]==target and right+1<=n:
                right+=1 
        elif left-1>=0 and right<=n and nums[left-1]==target:
            while nums[left-1]==target and left-1>=0:
                left-=1
        # elif nums[mid-1]==target and nums[mid+1]!=target and mid+1<=n and mid-1>=0:
        #     while nums[left-1]==target and left>=0:
        #         left-=1
        # elif nums[mid+1]==target and nums[mid-1]!=target and mid+1<=n and mid-1>=0:
        #     while nums[right+1]==target and right<=n:
        #         right+=1 
        else:
            while nums[left-1]==target and left-1>=0:
                left-=1
            while nums[right+1]==target and right+1<=n:
                right+=1
        ans[0],ans[1]=left,right
        return ans
    else:
        return [-1,-1]
    
    
    
l = searchRange([2,2,2,2,2],2)
print(l)