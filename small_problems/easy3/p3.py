'''
input: a string
output: a new string with each character doubled
rules:
    explicit: 
        - each character has to be doubled
    implicit
        - empty string should return zero
'''
'''
data structure
- a new string
'''
'''
ALG:
1. take the string
2. create a variable `result` and assign it to empty string
3. go through each character
4. append each character doubled to the result string
5. repeat for each character
6. return the result string
'''

def repeater(string):
    result = ''
    for char in string:
        result += char * 2
    return result

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True