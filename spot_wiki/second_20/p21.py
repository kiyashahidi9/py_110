'''
input: a list of nested lists of integers
output: a list with two integers

rules:
    - the output should be the location of the mine,
        - represented by 1
    - there is only 1 mine in the field 
    - the first integer should be nested list index
    - the second integer, the 1 within the nested list
    - there will always be a mine

data structure:
    - for loops

ALG:
1. take the list
1.. initialize row, column to 0
2. go through each nested_idx and nested_list
    - go through each num_idx and number in nested_list
    - if the number is 1
    - row is num_idx
    - column is nested_idx
    - break from the loop
return a list of row and column
'''

def mine_location(field):
    row, column = (0, 0)
    for nested_idx, nested_list in enumerate(field):
        for num_idx, number in enumerate(nested_list):
            if number == 1:
                column = num_idx
                row = nested_idx
                break
    return [row, column]

print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # should return [1, 1]
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]])) # should return [2, 1]
print(mine_location([[1, 0], [0, 0]])) # should return [0, 0]
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])) # should return [2, 2]