'''
input: string
output: a boolean True or False
    - depending on if the string is a palindrome
rules:
    explicit:
        - a palindrome is a word that is the same forwards and backwards
        - case matters
    implicit:
        - any character is counted, whitespace as well

questions:
    - if an empty string is passed?
'''

'''
Algorithm:
1. take the string as an argument 
2. create a `reverse_string` argument
    - initialize it to the string reversed, using slicing 
3. return if the string is equal to the reverse string
'''

def is_palindrome(string):
    reverse_string = string[::-1]
    return string == reverse_string

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)