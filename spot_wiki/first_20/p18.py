'''
input: an integer
output: an integer (multiplicative persistence)

rules:
    - how many times you need to multiply the digits 
        in the number until you reach a single digit
    - the individual numbers of the digit need to be mutliplied
    - given numbers already in single digits should return 0

data structure:
    - a list to extract the individual digits
    - an integer to keep track of how many times it has been multiplied


# step 2: 
# 1. take the integer
# 2. turn it into a string
# 3. split the string into a list of integers using a comprehension
# 4. return the list

# step 3:
# 1. take the list of digits
# 2. initialize a product variable to 1
# 3. for each num in the list, multiply product by num
# 4. return product

# step 4:
# 1. take the product
# 2. turn it into a string
# 3. if the length is one, return true
# 4. do this on a single line

# ALG:
1. take the integer
1.. intialize a count variable to 0
2. split it into a list of digits
3. mutliply each digit and take the product
4. if the product of the digits are a single digit, return count
5. if not, add to count and repeat step 2

'''

def persistence(integer):
    count = 0
    current_product = integer

    while True:
        if is_single_digit(current_product):
            return count
        else:
            count += 1
        digit_list = return_digit_list(current_product)
        current_product = return_list_product(digit_list)
    
def return_digit_list(integer):
    return [int(digit) for digit in str(integer)]

def return_list_product(digit_lst):
    product = 1
    for num in digit_lst:
        product *= num
    return product

def is_single_digit(number):
    return len(str(number)) == 1

print(persistence(33))

