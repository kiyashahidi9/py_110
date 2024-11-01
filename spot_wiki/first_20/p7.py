'''
input: a list of words
output: a string

rules:
    - the letters of the string should be the character of each string
        corresponding to its index position in the list
    - the 0 index character of the first word should be extracted
    - the 1 index character of the second word, etc.

data structure:
    - a string to hold the result
    - enumerate function to access both the index and the character

ALG:
1. take the list
1.. intialize a result string to ''
2. go through each word and its corresponding index
3. add the character at current index of the word to the result string
4. return the result string

step 2 and 3
1. for idx, word in enumerate(string)
    - result += word[idx]
'''

def nth_char(lst):
    result = ''
    for idx, word in enumerate(lst):
        result += word[idx]
    return result

print(nth_char(['yoda', 'best', 'has']))