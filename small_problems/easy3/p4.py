'''
input: a string
output: a different string
    - only consonants are doubled
rules:
    explicit:
        - only consonants are doubled
    implicit:
        - empty strings return empty strings
        - special characters are not doubled
'''
'''
data structures
- another string for the result
- a list of valid consonants
'''
'''
ALG
1. take the string
2. create an empty `result` string
3. go through each character
4. check if its a consonant
5. if it is, append to result string doubled
6. if not, append as is
7. return the result string

step 4
- create a constant list of `CONSONANTS`
- check for membership in the list
'''

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(string):
    result = ''
    for char in string:
        if char.casefold() in CONSONANTS:
            result += char * 2
        else:
            result += char
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")