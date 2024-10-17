'''
input: an integer
output: an integer
    - the sum of its individual digits

explicit rules:
    - the output has to be the sum of its individual digits
    - the input will always be a positive integer

data structures:
- string
- list of characters
- integer coercion

ALG:
1. take the integer
2. turn it into a string
3. split the characters into a list
4. make each character in the list an integer
5. return the sum of the list
'''

def sum_digits(integer):
    digit_list = list(str(integer))
    return sum([int(digit) for digit in digit_list])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True