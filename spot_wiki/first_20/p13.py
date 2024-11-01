'''
input: a CamelCase string
output: the string in kebab case

rule:
    - in camel case,
        words are separated by uppercase characters, no spaces
    - in kebab case
        words are separated by dashes, all lowercase
        - numbers are not included

data structure:
    - a list to keep track of the indeces of upper case characters
    - a string to have the final result

ALG:
1. take the string
1... intialize a result string
1.. go through each character, if the character is alphabetic, add to cleaned_string
    - list comprehension joined
3. go through each character and its index in cleaned_string
    - add the character lowercase to result
    - if the character after it is uppercase, 
        - add a '-' to result
4. return result
6. return step 5
'''

def kebabize(string):
    result = ''
    cleaned_string = [char for char in string if char.isalpha()]
    for idx, char in enumerate(cleaned_string):
        result += char.lower()
        if idx != (len(cleaned_string) - 1) and cleaned_string[idx + 1].isupper():
            result += '-'
    return result
print(kebabize('myCamelHas3Humps'))