'''
input: a string with number words
output: a string with number words converted to digit character

rules:
    - the number word has to be converted in its place to its digit character
    - there are no special characters
    - words are separated by spaces always

data structure:
    - a list to mutate the words
    - a dictionary to hold the corresponding digit values

ALG:
1. create a dictionary with number words and their digit values
2. split the string into a list of words
3. iterate through each word
4. if the word is in the dictionary,
    - the element should be reassigned to the value of the word
5. return the word list joined as a string
'''

def word_to_digit(string):
    
    number_words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    word_list = string.split()
    for idx, word in enumerate(word_list):
        if word in number_words:
            word_list[idx] = str(number_words[word])
        
    return ' '.join(word_list)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True