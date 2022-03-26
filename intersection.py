# def intersection(nums1, nums2):
#     for i in range(len(nums2)-2):
#         for j in range(len(nums1)-1):
#             if nums1[j] and nums1[j +1] in nums2[i:i+2]:
#                 return (nums1[j], nums1[j+1])

# print(intersection([2,2], [1,2,2,1]))



def intersection_(nums1, nums2):
    for j in range(len(nums1)-1):
        if nums1[j:j+2] in nums2:
            return (nums1[j:j+2])

print(intersection_([2,2], [1,2,2,1]))


#this way works but uses built in functions
def intersection_alt(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    print(set1, set2)

    return list(set1 & set2)

print(intersection_alt([2,2], [1,2,1]))