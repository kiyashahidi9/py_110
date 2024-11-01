'''
input: a string, a list of potential anagrams
output: a list of the anagrams

rules:
    - two words are anagrams if they both contain exactly the same letters
    - if there are no anagrams in the given list, an empty list should be returned

data structure:
    - a list

ALG:
1. take the string and potential_anagrams list
1.. initialize an anagram list to []
2. for each potential anagram
    - turn it into a list of characters
    - for each character in the string
        - check if the current char is in the list
            - if it is, remove the character from the list
            - if not, move on to the next potential anagram
    - if the list of characters is empty,
        - add the potential anagram to the anagram list
3. return the anagram list
'''

def anagrams(string, potential_anagrams):
    anagram_list = []
    for potential_anagram in potential_anagrams:
        if is_anagram(string, potential_anagram):
            anagram_list.append(potential_anagram)
    return anagram_list

def is_anagram(string, potential_anagram):
    char_list = list(potential_anagram)
    for char in string:
        if char in char_list:
            char_list.remove(char)
        else:
            return False
    return char_list == [] and len(string) == len(potential_anagram)

print(anagrams('laser', ['laesr']))