'''
input: a string
output: a substring of the string

rules:
    - the longest substring 
        - in which the characters are in alphabetical order

data structure:
    - a list

ALG:
1. Take the string
2. find all possible substrings
3. make a list with the substrings in alpha order
4. sort them by their length in descending order
5. return the first element of that list

step 2:
1. take the string
1.. initialize a result list
2. for each index1 in the length of the string
    - for each index2 in the length of the string after index 1
        - add each substring to the result list
3. return result list

step 3:
1. take the list of substrings
1.. initialize a result list
2. for each substring in the list
    - if substring equals sorted(substring)
        - add the substring to result
3. return result list

4. use the len and reverse=true keyword arguments
'''

def longest(string):
    all_substrings = return_all_substrings(string)
    alpha_sorted_substrings = return_alpha_sorted(all_substrings)
    sorted_list = sorted(alpha_sorted_substrings, key=len, reverse=True)
    return sorted_list[0]

def return_all_substrings(string):
    result = []
    for idx1 in range(len(string)):
        for idx2 in range(idx1, len(string)):
            result.append(string[idx1:idx2 + 1])
    return result

def return_alpha_sorted(substring_lst):
    result = []
    for substring in substring_lst:
        if list(substring) == sorted(substring):
            result.append(substring)
    return result

print(longest('asd'))                  # should return 'as'
print(longest('nab'))                  # should return 'ab'
print(longest('abcdeapbcdef'))         # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf')) # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag'))        # should return 'fgikl'
print(longest('z'))                    # should return 'z'
print(longest('zyba'))   



            
            
        