# All of these examples should print True
'''
input: a string
output: a list

explicit rules:
- each element of the list should be each character plus the last ones
- building incrementally

ALG:
1. take the string

'''

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])