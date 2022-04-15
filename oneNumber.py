
# O(n) runtime, only one constant extra space
def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    n = sorted(nums)
    print(nums, '>>', n)
    
    for i in range(len(nums)-1,-1, -1):
        # print(n[i])
        if n[i] != n[i-1] and i ==len(n)-1:
            return n[i]
        if i != len(n)-1:
            if n[i] != n[i-1] and n[i] != n[i+1]:
                return n[i]
       
    return False


print(singleNumber([1]))