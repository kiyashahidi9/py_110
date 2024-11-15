'''
input: a string
output: the highest scoring string

rules:
    - each letter scores based on its position in the alphabet
    - each letter adds to the total score of the word
    - the word with the highest score should be returned
    - input will always be lowercase

data structure:
    - a list to keep track of the scores
    - a string to keep track of each letters points

ALG:
1. take the string
2. initialize an alpha_point string, with a starting at index 1
2.. initialize a scores_list
3. split the string into a list of words
4. for each word
    - initialize a score variable
    - for each char in the word
        - add the score of the char to score variable
    - add the score to a scores_list
5. find the index of the highest score
6. return the word at that index in the string

step 5.
- take the scores_list
- find the max value
    - .index method to find the idx of max value
- return idx of max value
- USE HELPER FUNCTION
'''

def high_score_idx(score_list):
    return score_list.index(max(score_list))

def high(string):
    alpha_point = '!abcdefghijklmnopqrstuvwxyz'
    string_list = string.split()
    score_list = []

    for word in string_list:
        score = 0
        for char in word:
            score += alpha_point.index(char)
        score_list.append(score)

    return string_list[high_score_idx(score_list)]

print(high('aaa d'))
