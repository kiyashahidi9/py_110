'''
input: a string of text
output: a list of words 

rules:
    - the list should be the top 3 most common words that occur
    - it should be ordered in descending order
    - word matches should be case-insensitive
    - if there are less than 3 words, the top 2 or top 1 should be returned
    - if a word is just punctuation, it isn't counted as a word
    
data structure:
1. a dictionary to keep track of how often each word occurs
2. a list to track the occurences and the word
    - this can be sorted

ALG:
1. take the string
2. initialize an empty dict word_occurences
2.. intialize a list of the words 
3. go through each word, count how many times they occur
4. update the dictionary accordingly
5. go through the dictionary, add the count, word tuples to a list
6. sort the list by descending order and by the count
7. return a list of the first three words of the list

step 3:
1. with a for loop, iterate through the list of words
    - each word is casefolded
1.. if the word is just punctuation, don't do step 2
2. assign the key to the .get() of the key, if the key doesn't exist,
    - make the default 0
    - increment the value by 1

step 5:
1. use a comprehension

step 7:
1. if the length of lst is >= 3, return a list of the first three counts
    - using a comprehension, iterating through both the count and word
2. if not
    - return a list of all of the words in its order
'''

def top_3_words(string):
    word_occurences = {}
    word_list = [remove_end_punc(word) for word in string.split()]

    for word in word_list:
        word = word.casefold()
        if is_word(word):
            word_occurences[word] = word_occurences.get(word, 0) + 1
    
    word_count_list = [(count, word) for word, count in word_occurences.items()]
    word_count_list.sort(reverse=True)
    
    top_list = return_top_x_list(word_count_list)
    return top_list

def is_word(word):
    for char in word:
        if char.isalpha():
            return True
    return False

def remove_end_punc(word):
    if not word[-1].isalpha():
        return word[:-1]
    return word

def return_top_x_list(lst):
    if len(lst) >= 3:
        return [lst[top][1] for top in range(3)]
    else:
        return [word for count, word in lst]

print(top_3_words('''In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""" '''))
