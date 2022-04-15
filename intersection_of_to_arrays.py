def intersection(nums1, nums2):
    # match= []
    # for i in nums1:
    #     for j in nums2:
    #         if i == j:
    #             match.append(i)
    #             break 


    num1Dict={}
    for i in nums1:
        # check to see if value is already a key, if so add to value count
        if i in num1Dict:
            num1Dict[i] += 1

        #if value is not a key, set it to key:1.  first occurences
        else:
            num1Dict[i] = 1

    print(num1Dict)
    match=[]
    for j in nums2:
        if j in num1Dict:
            if num1Dict[j] != 0:
                match.append(j)
                num1Dict[j] -= 1
    print(match)



intersection([1,2,2,3,4,4], [3,2,5,2,1,1])




