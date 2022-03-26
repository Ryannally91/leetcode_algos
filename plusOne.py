# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(arr):
    arr[len(arr) - 1] = arr[len(arr) - 1] + 1
    if arr[len(arr) - 1] == 10:
        for i in range(1,len(arr)):
            if arr[len(arr) - i] == 10:
                arr[len(arr) - (i+1)] += 1
                arr[len(arr) - i] = 0
        return arr
    
    return arr

print(plusOne([1,2,9]))


#output [1,3,0]  carried over.  dont know if thats what it was asking