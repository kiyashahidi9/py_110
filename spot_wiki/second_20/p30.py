'''
input: two strings
output: True if the two strings are anagrams of eachother

rules:
    - if the words have exactly the same letters, case insensitive,
        - they are anagrams

Data Structure:
    - a list to keep track of the letters

ALG:
1. take the two strings
2. split the characters in the first string into a list
    - make the characters case insensitive
3. go through the characters in the second string
    - if the character (case insensitive) is in the list
        - remove the character from the list
    - if the character (case ins) is NOT in the list
        - return False
4. return if the list is empty
'''

def is_anagram(str1, str2):
    str1_lst = [char.casefold() for char in str1]
    str2 = str2.casefold()

    for char in str2:
        if char in str1_lst:
            str1_lst.remove(char)
        else:
            return False
        
    return str1_lst == []

print(is_anagram('Creaetive', 'ReactiEve'))