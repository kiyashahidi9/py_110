'''
input: two lists
output: a set
    - the union of the values of the two lists
explicit rules:
    - the function will return a set
'''
'''
data structure:
- set

algorithm:
1. take the two lists
2. convert both lists to sets
    - set() constructors
    - initialize to variables `set1` and `set2`
3. return the union of those sets
'''

def union(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 | set2

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True