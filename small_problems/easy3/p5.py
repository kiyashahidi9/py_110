'''
input: a positive integer
output: a different integer
    - the numbers reversed
'''
'''
data structures:
- make a string so you can reverse it
'''
'''
ALG:
1. take the number
2. turn it into a string
3. reverse the string
4. turn it back into an integer
5. return the integer
'''

def reverse_number(integer):
    return int(str(integer)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
