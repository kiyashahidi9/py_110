'''
input: a string integer
output: an integer with each digit from the string

rules
    - not allowed to use int() function
    - each digit has to be converted to an integer
    - the number should be mutliplied by its place (thousands place, hundreds place)

data structure
    - dictionary to hold the corresponding integers

ALG:
1. take the string
2. create a dictionary with the corresponding integers to each digit character
2.. initialize a result variable to 0
2... initialize a `place` variable to 10 to the power of the length of the string minus 1
3. go through each character in the string
4. find its corresponding integer
5. multiply the corresponding integer by the appropriate place
6. add that to the result
7. repeat 4 to 6
8. return result

step 5:
1. determine the length of the string
3. multiply the corresponding integer by place
4. divide place by 10
'''

def string_to_integer(string):
    digit_to_int = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    result = 0
    place = 10**(len(string) - 1)
    for num in string:
        result += digit_to_int[num] * place
        place //= 10

    return result

def string_to_signed_integer(string):
    if string[0].isdigit():
        return string_to_integer(string)
    elif string[0] == '+':
        return string_to_integer(string[1:])
    else:
        return -(string_to_integer(string[1:]))
    
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True