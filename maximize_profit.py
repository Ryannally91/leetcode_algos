
# [5,3,4,7,4,8] -->8
def maximize(nums):
    profit=0
    for i in range(len(nums)-1):
        if nums[i] <nums[i +1]:
            profit += nums[i+1] - nums[i]

    return profit

print(maximize([5,3,4,7,4,8,3,3,100]))
