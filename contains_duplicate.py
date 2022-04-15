# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in nums:
#             if i in nums[i +1:]:
#                 return True
#         return False


#not passing leetcod, times out
def containsDuplicate(nums):
        if len(nums) ==1:
            return False
        for i in range(1,len(nums)):
            if nums[i-1] in nums[i:]:
                
                return True
            print(nums[i:])
        return False
print(containsDuplicate([3,2,1]))

#passed all
def containsDup(nums):
    if len(nums) < 2:
        return False
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(containsDup([2]))

#should also work
def containsDuplicates(arr):
    if set(arr) != arr:
        return True


def rae(arr):
    new= list(filter(lambda x: x != 2, arr))
    print(new)

rae([1,2,3,4])
