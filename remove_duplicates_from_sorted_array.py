# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(nums):
        count = 1 #already 1 unique value
        last_unique = nums[0]#use a two-pointer method:  one points to current value, the other points to lastUniqueValue  (right pointer)
        next = 1 #index of where to place next unique values  (left pointer)
        for i in range(1,len(nums)):
            if nums[i] != last_unique:
                nums[next]= nums[i]
                next += 1    #go to next index
                count += 1
                last_unique = nums[i]
        print(nums)
        return (next) #just need to reutrn k.  next takes care of count.  COunt is not needed
            
            

print(Solution.removeDuplicates([1,1,2,3,4,4,4,5,6,6]))