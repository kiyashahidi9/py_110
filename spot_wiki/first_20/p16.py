'''
input: a string with words
output: a string

rules
    - the words that have 5 or more letters should be reversed
    - other words should stay the same

data structure
    - a list to hold the words

ALG:
1. take the string
2. split the words into a list
3. go through each word and its index
    - if the word has 5 or more characters, 
        - the current word should be reversed
4. return the word list joined by spaces

step 3.
1. iterate using a for loop and enumerate function
2. if the len(word) is 5 or more
    - list[current_idx] = word[::-1]
'''

def spin_words(string):
    word_list = string.split()
    for idx, word in enumerate(word_list):
        if len(word) >= 5:
            word_list[idx] = word[::-1]
    return ' '.join(word_list)

print(spin_words('hey fellow warriors'))

