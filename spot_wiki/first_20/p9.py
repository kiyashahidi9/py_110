'''
input: a string of words
output: a string with each word scrambled

rules:
    - the first and last characters stay where they started
    - the punctuation should stay where they started
        - the letters before and after the punctuation should be sorted separately
    - the characters in between the first and last character should be sorted alphabetically

data structure:
    - a list of the original words 
    - a list of the characters
    - a list of the punctuation and its index

ALG:
1. take the string
2. split the words of the string into a list
3. go through each word, scramble it accordingly and add to a result list
4. return the result list joined by spaces

step 3:
# 1. take the word
# 1.. intialize a punctuation list
# 1... initialize a mid_chars list
# 1.... initialize a first, last character variable
    # - if the last character is a comma or a period, 
    #     - the second to last character and the last character is the variable
2. go through each character and its index,
    - if the character is not alphabetic,
        - append a tuple (idx, punctuation)
    - if the character is not the first, or last letter and is alphabetic,
        - append it to mid_chars list
3. sort the mid_chars list
4. for each item and its index in the punctuation list, 
    insert it into the correct index
5. return an fstring of the first_char, mid_chars list joined, the last_char

'''

def scramble_words(string):
    return ' '.join([scramble_word(word) for word in string.split()])

def scramble_word(word):
    punctuation_list = []
    mid_chars = []
    first_char = word[0]
    last_char, last_idx = return_last_char(word)

    for idx in range(1, last_idx):
        if word[idx].isalpha():
            mid_chars.append(word[idx])
        else:
            punctuation_list.append((idx, word[idx]))

    mid_chars.sort()

    for idx, punc in punctuation_list:
        mid_chars.insert(idx - 1, punc)

    return f'{first_char}{''.join(mid_chars)}{last_char}'

def return_last_char(word):
    if word[-1].isalpha():
        return (word[-1], len(word) - 1)
    else:
        return (word[-2:], len(word) - 2)
    
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))