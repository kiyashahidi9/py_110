'''
input: a list of integers
output: the average of that list
'''
'''
ALG
1. take the list
2. add all the numbers to a total
3. assign that total to variable `sum_`
4. return sum_ // by the length of the list 

implementation
2. sum() function
'''
def average(lst):
    return sum(lst) // len(lst)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
