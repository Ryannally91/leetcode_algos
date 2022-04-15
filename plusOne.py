# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(arr):
    arr[len(arr) - 1] = arr[len(arr) - 1] + 1
    if arr[len(arr) - 1] == 10:
        for i in range(1,len(arr)):
            if arr[len(arr) - i] == 10:
                arr[len(arr) - (i+1)] += 1
                print(arr)
                arr[len(arr) - i] = 0
        if arr[0] == 10:
            arr.insert(0, 1)
            arr[1]= 0
        print(arr)
        return arr
    
    return arr

print(plusOne([9,9,9]))
print(25.25)
print(float(25.25))

#output [1,3,0]  carried over.  dont know if thats what it was asking

# leetcode
# mine
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits[len(digits) - 1] = digits[len(digits) - 1] + 1
#         if digits[len(digits) - 1] == 10:
#             if len(digits) == 1:
#                 digits= [1,0]
#                 return digits
#             for i in range(1,len(digits)):
                
#                 if digits[len(digits) - i] == 10:
#                     digits[len(digits) - (i+1)] += 1
#                     digits[len(digits) - i] = 0
#                 if digits[0] == 10:
#                     digits.insert(0,1)
#                     digits[1]=0
#             return digits

#         return digits

