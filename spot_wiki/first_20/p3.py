'''
input: 2 strings, a full text, and a search text
output: integer

rules:
    - the integer should be the amount of times search text occurs in full_text

data structure:
    - strings
    - .count() method

ALG:
1. take the full text and search text
2. return the fulltext with the count method invoked
    - the argument search text provided
'''

def solution(full_text, search_text):
    return full_text.count(search_text)

print(solution('abcdeb','b'))
print(solution('aaabbbcccc', 'bbb'))