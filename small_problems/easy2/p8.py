'''
input: an integer
output: a list of integers of each individual digit of the original integer
'''
'''
data structure
- convert original integer to string
'''
'''
ALG
1. take the integer
2. convert it into a string
3. assign that to a variable `string_int`
3. initialize an empty list, `result`
4. iterate through each character
5. append it to `result` back as an integer
6. return `result`
'''

def digit_list(int1):
    return [int(digit) for digit in str(int1)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
