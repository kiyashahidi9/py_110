'''
input: a string
output: a list of pairs

rules:
    - the string should be split into pairs 
    - if the string has an odd number of characters, 
        - its last character should be paired with an underscore
    - an empty string should return an empty list

data structure:
    - a list
    - indexing and slicing

ALG:
1. take the string
1.. initialize a result list to []
2. iterate through the indexes with a range to the -1 index with a step of 2
    - for each iteration, append the current index plus the next index to result list
3. if the length of string is odd
    - append the last character and an underscore
5. return the result list
'''

def solution(string):
    pairs = []
    for idx in range(0, len(string) - 1, 2):
        pairs.append(string[idx:idx + 2])
    if len(string) % 2 != 0:
        pairs.append(f'{string[-1]}_')
    return pairs

print(solution('abcdefae'))