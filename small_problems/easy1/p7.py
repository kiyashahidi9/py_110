'''
input: a string of space separated words
output: the string 
    - with first and last letters swapped
rules:
    explicit:
        - case stays
        - first and last letters are swapped
'''
'''
data strucutres
- list
    to manipulate individual words
'''
'''
ALGORITHM:
1. create a `result` variable and initialize it to an empty string
2. create a `list_words` variable and initialize it to a list of the words in the string
3. swap the first and last letter of each word in the list
4. join the words back into the result string
5. return the result string

step 3: swap the first and last letter
1. for each word in lst
1. create two variables: `first_letter` and `last_letter`. Initialize to 0 and -1 indexes
2. equal the first index to last letter, and last index to first letter
'''

def swap(string):
    list_words = string.split()
    result_list = []
    for word in list_words:
        if len(word) != 1:
            new_word = f'{word[-1]}{word[1:-1]}{word[0]}'
        else:
            new_word = word
        result_list.append(new_word)
    return ' '.join(result_list)

print(swap('Oh what a wonderful day it is')
       == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")          # True
