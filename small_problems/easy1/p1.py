'''
input: six integers
output: a string 
    - confirms or denies that the last number is in the first 5
rules:
    explicit:
        - the last number has to be checked if its in the first 5
        - input gathered from the user
    implicit:
        - any positive integer is valid

questions:
- should i handle invalid input cases?
'''
'''
Data structure:
- a list of integers
- checking for membership

Algorithm:
1. gather input for all 6 numbers, assign each to a variable
2. assign a list to the value of the first 5 numbers
3. check for membership of the last number in the list
4. print the outcome

step 3 and 4
- assign a variable to a boolean value using the 'in' keyword
- conditional if block to determine which outcome is printed
'''

num1 = input('Enter the 1st number: ')
num2 = input('Enter the 2nd number: ')
num3 = input('Enter the 3rd number: ')
num4 = input('Enter the 4th number: ')
num5 = input('Enter the 5th number: ')
last = input('Enter the last number: ')

num_list = [num1, num2, num3, num4, num5]
is_in_list = last in num_list

if is_in_list:
    print(f'{last} is in {','.join(num_list)}.')
else:
    print(f'{last} isn\'t in {','.join(num_list)}.')