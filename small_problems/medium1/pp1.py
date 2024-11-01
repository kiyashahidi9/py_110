'''
input: a list
output: a different list

explicit rules:
    - the first element is now the last element
    - the two lists are different
    - if a given argument is not a list, return None

data structure:
    - a shallow copied list 

ALG:
1. take the input list
2. check if input is an instance of list, if not, return None
2. create a copy of the list
3. pop the first element and capture it as the rotated_element
4. append the rotated element to the list
5. return the list
'''

def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if not lst:
        return []

    return lst[1:] + [lst[0]]


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# # return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# # the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])