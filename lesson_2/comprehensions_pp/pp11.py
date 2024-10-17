'''
input: a dict with nested lists
output: a list

explicit rules:
    - every vowel from each sublist is in the list

ALG:
1. take the dict
2. go through each sublist value
3. go through each character, and append to a result list if is vowel
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def list_of_vowels(dictionary):
    result = []
    vowels = 'aeiou'
    for word_lst in dictionary.values():
        for word in word_lst:
            for char in word:
                if char in vowels:
                    result.append(char)
    return result

vowels = 'aeiou'

list_vowels = [char for word_lst in dict1.values()
               for word in word_lst
               for char in word if char in vowels]

print(list_of_vowels(dict1))
print(list_vowels)
# # ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']