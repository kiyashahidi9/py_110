'''
input: a string
output: a dictionary

rules:
    - the key should be the number of occurences
    - the value should be a list of characters that occured `key` times
    - special characters, spaces should be ignored
    - characters should be casefolded
    - the dictionary keys should be sorted by largest number first
    - the character lists should be sorted in alphabetic order

data structures:
    - list
    - dictionary

ALG:
# 1. take the string
# 1.. initialize a count dictionary
# 2. create a cleaned up string with only casefolded, alphabetic characters
# 3. count the occurence of each character and update count dictionary
# 3.. initialize a result dictionary
# 4. go through each count in the count dictionary
#     - add a key of each unique count to result
#     - set the value to an empty list
5. go through character and count in the count dictionary
    - if the count is a key in result,
        - append the character to its list
6. go through each list in result and sort it alphabetically
7. sort the keys in descending order
8. return the result list

step 7:
1. change the key:value pairs into a list of tuples
    - list()
2. sort the list
3. return the list as a dict

'''

def get_char_count(string):
    cleaned_string = clean_string(string)
    count_dict = {}
    for char in cleaned_string:
        count_dict[char] = count_dict.get(char, 0) + 1
    result = {}

    for count in count_dict.values():
        result[count] = []
    
    for char, count in count_dict.items():
        if count in result:
            result[count].append(char)

    for list in result.values():
        list.sort()

    return sort_dict(result)
    
def sort_dict(dict_):
    return dict(sorted(list(dict_.items()), reverse=True))

def clean_string(string):
    result = ''
    for char in string:
        if char.isalpha() or char.isdigit():
            result += char.casefold()
    return result

print(get_char_count("Mississippi")) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!")) # should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!")) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc")) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123")) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}