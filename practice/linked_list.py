
def majorityElements(nums):
        
    d = {}
    for i in nums:
        if i not in d.keys():
            c = 1
            d[i] = c
        d[i] = d[i]+1
    m = max(d.values())
    for i in d.keys():
        if d[i]==m:
            print(i)
            break
        
nums = [2,3,2,4,5,3,5,5]
majorityElements(nums)