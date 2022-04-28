def rotate_img(matrix):
   
    for x in range(len(matrix)):
        r= (len(matrix[x])-(1+x))
        # for y in range(len(matrix[x])):
        matrix[x][r], matrix[r][r], matrix[r][x],matrix[x][x] =  matrix[x][x], matrix[x][r], matrix[r][r], matrix[r][x]
        print(matrix)


#My attempt didnt work

matrix = [[1,2,3],[4,5,6],[7,8,9]]


# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 
# rotate_img(matrix)

#solution https://www.google.com/search?q=rotate+image+leetcode+python&oq=rotate+image+leetcode+python&aqs=chrome..69i57.13833j1j7&sourceid=chrome&ie=UTF-8#kpvalbx=_Yz9UYpa-L9zEqtsP0J2muAw16
#rotating in reverse order allows or less temporary variable

def rotate_image(matrix):
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r -l):
            print(i)
            top, bottom = l, r
            # save top left #reduces number of temp var you'll need. 
            topLeft = matrix[top][l + i] #this is temp var that will be used at end
            #move bottom left into top left
            matrix[top][l + i ] = matrix[bottom- i][l]
            #move bottomr right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r-i]
            #move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]
            # move top left into top right
            matrix[top + i][r] = topLeft
            print(matrix)
        r -= 1 #These  increment in order to target inner sections
        l += 1
        
        return matrix

print(rotate_image(matrix))

#this approach utilizes to pointer.  after each loop you offset poisitons by i.
# after after loop, move to inner loop,  r-=1 and l+=1, shift every thing to the next inner square