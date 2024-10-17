'''
input: a list of one or more strings
output: a new list of same string values
    - with vowels removed

explicit rules:
    - the vowels must be removed
    - the same amount of elements as the original list

data structures:
- a list 

ALG:
1. take the list
2. go through each element
3. remove the vowels from each element
4. add the cleaned up words to a list
5. return the cleaned up list

step 3 and 4
1. take the string
1.5: intialize a result variable
2. iterate through each character
    - if it is not a vowel, append to a result string
3. return the cleaned up string
'''

def clean_word(string):
    result = ''
    VOWELS = 'aeiou'
    for char in string:
        if char.casefold() not in VOWELS:
            result += char
    return result

def remove_vowels(lst):
    return [clean_word(string) for string in lst]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True