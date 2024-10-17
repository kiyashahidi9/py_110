'''
input: a list
output: a list with two nested lists
    - split in half
rules:
    explicit:
        - if the list is odd, place the middle element in the first list
        - the first half of elements 

questions:
- should we return the same list object?
'''
'''
ALGORITHM
1. take the list object
2. create half1, half2 variables and initialize them to empty lists
2.5. create `half point` variable
    - the length of list // by two
3. if the length of the list is even, half1 is the first half, half2 the second half
4. if odd, include the middle element in the first half, and the rest in the second half
6. return result list

step 3
- use list slicing, not including the half point

step 4
- use list slicing, including the half point
'''

def halvsies(lst):
    half_point = (len(lst) + 1) // 2
    half1 = lst[:half_point]
    half2 = lst[half_point:]
    return [half1, half2]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])