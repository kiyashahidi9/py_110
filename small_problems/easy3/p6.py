'''
input: an integer
output: a list
    - from 1 to the integer inclusive, incrementing by 1

data structures
- a range to capture the integers
- a list to create the element values of the range

ALG
1. take the integer
2. create a range from 1 to the integer plus 1
3. turn that range into a list
4. return the list
'''

def sequence(integer):
    return list(range(1, integer + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True