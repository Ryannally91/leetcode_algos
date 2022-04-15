def rotate(nums, k):
    if k > len(nums):
        k = k % len(nums)
    for i in range(k):
        r = (len(nums)-1)
        print(r)
        temp= nums[r]
        for j in range(r, -1, -1):
            print(nums[j])
            nums[j]= nums[j-1]
        nums[0]=temp
        print(nums)        
    return nums


# print(rotate([1,2,3,4], 2))

#^^^^^^^^Works but times out on large inputs


def rotate_arr(nums, k):
    k = k % len(nums) #reduce unnessecary rotations
    print(k)

    ##reverse entire array
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1
        r -= 1
    # to correct order, re-reverse section k to end
    l, r = k, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1
        r -= 1
    # to correct order, re-reverse section begining to k
    l, r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1
        r -= 1

    print(nums) 
    return nums

rotate_arr([1,2,3,4], 2)

##thought process
#in example above  [1,2// 3,4] >  [3,4, 1,2]
#split arr at k, and move back portion to front.
#to accomplish in code, reverse entire array, the reverse sections [:k], [k:]