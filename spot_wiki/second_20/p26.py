'''
input: two lists
output: an integer

rules:
    - each corresponding index should be subtracted from eachother
        - the difference taken the absolute value of
        - then squared
    - add all of these integers and take the average
    - the number of objects in each list is always the same

data structure
    - a list to hold the squares

ALG:
1. take list1 and list2
1.. initialize squares list
2. go through the indexes in a range to the length of list1
3. subtract the current index in list1 by current index in list2
4. take the absolute value of that
5. square it
6. add that number to a squares list
7. repeat steps 2 to 6
8. return the average of the squares list

step 8.
1. find the sum of the squares list
2. divide by the length
'''

def solution(lst1, lst2):
    squares = []
    for idx in range(len(lst1)):
        squares.append((abs(lst1[idx] - lst2[idx]))**2)
    return sum(squares) / len(squares)

print(solution([1, 2, 3], [4, 5, 6]))
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))
print(solution([-1, 0], [0, -1]))