# SELECT department.dept_id, count(employee.emp_id) as count, sum(employee.salary) as sum_of_salary
# FROM department
# JOIN employee ON department.dept_id = employee.dept_id
# GROUP BY department.dept_id
# ORDER BY department.dept_id;

def solution(S):
    blocks_count = []
    count = 1
    for i in range(len(S)):
        print(S[i])
        if i == len(S)-1:
            # count +=1
            blocks_count.append(count)
            print('im here')
        elif S[i] != S[i-1]:
            blocks_count.append(count)
            count =1
            # print(count)
      
        else:
            count += 1
        # print(count)
    _max = max(blocks_count)
    print(blocks_count)
    differences = []
    for num in blocks_count:
        # print(_max - num)
        differences.append(_max - num)
        print(differences)
    print(sum(differences))
    return sum(differences)
    #find max in count list
    #subtract absVal of count and max count
    #add differences 

solution('bbbab')

# you are in a browser like environment, where you will have access to the window object, the documant object, and also $....Each cell of the table has an upper-case letter in it and has its background
def alt_solution(S):#######using a list,  i did not have same issue as before
    list_str=[]
    for i in S:
        list_str.append(i)
    print(list_str)
    lengths=[]
    count =1
    for i in range(len(list_str)):
        if i == len(S)-1:
            lengths.append(count)
            print('im here')
        elif S[i] != S[i+1]:
            lengths.append(count)
            count =1
        else:
            count += 1
        print(lengths)
    sum_=0
    max_ = max(lengths)
    for num in lengths: 
        sum_ += (max_-num)
    print(sum_)
    return sum_
alt_solution('aabbababbb')

##^^^^^^ This works