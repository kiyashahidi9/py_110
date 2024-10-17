'''
input: a string consisting of zero or more space separated words
output: a dictionary
    - key: the size of the word
    - value: how often that size word occurs
rules:
    explicit:
        - words are only alphabetic letters
        - each different sized word will have its own key
        - words of the same size belong to the same key
            - increment the values
'''
'''
data structures:
- dictionary

algorithm:
1. create a `result` variable to an empty dictionary
2. exclude non-letters from string
2. add how many times a certain length word occurs in the dictionary to result
3. return `result`

step 2
1. count each word
    - convert the string to a list separated by spaces
    - iterating through the words with a for loop
2. if that count exists, increment the value
3. if not, create a new size key and set it to 1
    - .get() method with a default of 0, adding 1

step 2.5: get rid of non-letters
1. intiialize a `cleaned_list` variable to an empty list
1. iterate through each element in the new string
2. initialize a `cleaned word` variable to an empty string
3. iterate through each character
4. if the char is alphabetic, append it to cleaned word
5. add cleaned word to `cleaned list`
6. return `cleaned list`
'''

def clean_words(lst):
    cleaned_list = []
    for word in lst:
        cleaned_word = ""
        for char in word:
            if char.isalpha():
                cleaned_word += char
        cleaned_list.append(cleaned_word)
    return cleaned_list

def word_sizes(string):
    result = {}
    string_list = clean_words(string.split())

    for word in string_list:
        result[len(word)] = result.get(len(word), 0) + 1

    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})