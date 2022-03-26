#[1,0,2,3,0,2,1] >>>>[1,2,3,2,1,0,0]


def moveZeros(arr):
    l = 0 #moves through arr only when element is non zero
    for r in range(len(arr)):
        if arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l +=1
    return arr

#Quicksort, 2-pointere

#right keeps on moving, once it sees a non-zero val it will swap with left pointer. 
#  Left pointer only increments when its not pointing to a zero

#https://www.youtube.com/watch?v=aayNRwUN3Do&t=39s``

print(moveZeros([1,0,2,3,0,2,1]))