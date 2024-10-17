'''
input: a list of integers
output: a string 
    - the number of getting the multipicative average
rules:
    explicit:
        - multiplying all the elements of the list, diving by the length of the list
'''
'''
ALGORITHM
1. take the list
2. multiply all the numbers in that list
3. assign that value to a `sum` variable 
4. divide the sum by the length of the lst
5. assign that value to a multiply average variable
6. return `multiply average` variable coerced into a string, formatted to 3 decimal places
'''

def multiplicative_average(lst):
    product = 1
    for element in lst:
        product *= element
    multiply_average = product / len(lst)
    return f'{multiply_average:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")