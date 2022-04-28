# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#brute Force )(n^2) 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i + j == target and i != j:
#                     return i , j

'''
most optimal -one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
'''
# my version
'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addends={}
        for i in range(len(nums)):
            key_= target-nums[i]
            if key_ in addends:
                return [i, addends[key_]]
            addends[nums[i]] = i  #here you want to add val: index  Not Target - currVal
            '''

k= [3,5,2,7,1,8,4]
print(sorted(k))
def twoSum(nums, target):
    r = len(nums)-1
    # sort list 
    _nums = sorted(nums)
    values = []
    print(nums, '--->', _nums)
    l= 0
    # print(nums.sort())
    for i in range(len(_nums)):
        print(l, "--", r)
        print(_nums[l], '+' , _nums[r])
        if _nums[l] + _nums[r] == target and l != r:
               
                if _nums[l] == _nums[r]: #######for edge cases [3,3] index() finds first instance unless given a second arguemnet
                    x = nums.index(_nums[l])
                    y = nums.index(_nums[r], x +1)
                    return (x, y )
                else:
                    return (nums.index(_nums[l]), nums.index(_nums[r]))
        elif _nums[l] + _nums[r] > target:
            r -= 1
            print(i, '----', r)
        else:
            l += 1
    # nums.index(value)

print(twoSum([1,2,4,3,6], 6))
print(twoSum([3,3], 6))

#works^^^^^ phew!