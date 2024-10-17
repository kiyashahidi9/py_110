'''
Algorithm:
1. remove all the non-alphanumeric characetrs
2. make the string case insensitive
3. return the is_palindrome call

step 1:
1. initialize a result string variable to an empty string
1. iterate through all the characters,
2. if character is alphanumeric, append to result string
3. casefold result string
3. return result string
'''

def remove_non_alphanumeric_char(string):
    result = ''
    for char in string:
        if char.isalnum():
            result += char
    result = result.casefold()
    return result

def is_real_palindrome(string):
    modified_string = remove_non_alphanumeric_char(string)
    return is_palindrome(modified_string)

def is_palindrome(string):
    reverse_string = string[::-1]
    return string == reverse_string

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True