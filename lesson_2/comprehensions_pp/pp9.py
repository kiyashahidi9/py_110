'''
ALG
1. go through each subdict of the lst
2. return that subdict to a new lst if it meets the conditions

step 2
1. go through each list value in the subdict
2. check if all of the numbers are even
3. return a boolean true or false
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def lst_is_not_even(lst):
    for num in lst:
        if num % 2 != 0:
            return True
    return False

def is_even(subdict):
    for sublst in subdict.values():
        if lst_is_not_even(sublst):
            return False
    return True
        
even_lsts = [subdict for subdict in lst if is_even(subdict)]

print(even_lsts)

