

def isValidSudoku(board):
    #check column
    for i in range(len(board[0])):
        for j in range(len(board)):
            # print(i,'>>>>>>', j, '>>>', board[j][i])
            for k in range(j+1,len(board)):
                # print(board[k][i])
                if board[j][i] ==board[k][i]:
                    if board[j][i] != '.':
                        return False

    # check rowS
    for row in range(len(board)):
        for i in range(len(board[0])):
            if board[row][i] in board[row][i+1:-1]:
                if board[row][i]!= '.':
                    return False
    start = 0
    end = 3
    check_list=[]
    for val in range(start,end):
        for i in range(start, end):
            if board[val][i] != '.':
                check_list.append(board[val][i])
            print(check_list,'iiii', set(check_list))
        if len(check_list) != len(set(check_list)):
            return False
    #could recursively call itself
    # else:
    #     start
    
    return True
    #check 3x3 box
    
    

board = [["8",".",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".","5","."]
        ,[".","9",".",".",".",".",".","6","."]
        ,[".",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

#The above is a lot of code.  Below is the ideal version using a hash table

#Use collections library
#defaultdict(set) creates a dictionary with default values of empty sets.

import collections

def checkBoard(board):
    col = collections.defaultdict(set)
    row = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            print(col,'||||', row, '||||', squares, "||||")
            if board[r][c] != '.':
                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in squares[(r //3, c // 3)]:
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
    
    return True

print(checkBoard(board))

def sudako(board):
    rows=collections.defaultdict(set)
    col=collections.defaultdict(set)
    squares=collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] != '.':
                if board[r][c] in rows or board[r][c] in col or board[r][c] in squares:
                    return False
                #add to dictionaries
    
