'''
input: a string
output: a boolean

rule:
    - if the string has every letter of the alphabet, 
        the output should be true
    - otherwise, output should be false
    - keep track of the letters used
    - keeping track of the letters should be case insensitive

data structure:
    - a dictionary of what letters have been used

ALG:
1. initialize a dictionary of all letters as keys, and values to 0
2. go through the string, for each character
    - if the character casefolded exists in the dictionary,
        - increment occurence by 1
3. determine if all of the letters have occured at least once
4. return that boolean value

step 1. create alpha_dict
1. create a string of the alphabet
2. for each character, create a key of that character with the value equal to 0

step 3. 
1. use the all() function for the values in the dictionary
'''

def create_alpha_dict():
    alpha = 'abcdefghijklmnopqrstuvwxwz'
    return {char: 0 for char in alpha}

def panagram(string):
    alpha_dict = create_alpha_dict()
    for char in string:
        char = char.casefold()
        if char in alpha_dict:
            alpha_dict[char] += 1
    return all(alpha_dict.values())


