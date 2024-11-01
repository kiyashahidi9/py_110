'''
input: a string of an integer
output: an integer

rules:
    - the integer should represent the number of all possible substrings
        that are odd when converted to an integer
    - the substrings are calculated from index 0, index 0 to 1, index 0 to 2 etc
    - and then moves on to index 1, index 1:2, index 1:3, so on

data structure:
    - a list to hold all of the possible substrings
    - convert to an integer to evaluate if its odd

ALG:
1. take the string of integers
1.. initialize a odd num count to 0
2. find all possible substrings and add to a list
3. go through each substring in the list and convert to an integer
4. if its odd, add to a count
5. return the count

step 2:
1. take the string of integers
1.. initialize an substring_list
2. go through each letter
    - for each letter, go through each letter after it
- for idx1 in range(len(string))
    - for idx2 in range(len(string))
        - odd_list.append(string[idx1:idx2 + 1]) # end is non inclusive
3. return substring_list
'''

def return_substring_list(string):
    substring_list = []
    for idx1 in range(len(string)):
        for idx2 in range(idx1, len(string)):
            substring_list.append(string[idx1:idx2 + 1])
    return substring_list

def return_odd_substrings_in_string(string_ints):
    substring_list = return_substring_list(string_ints)
    odd_count = 0
    for substring in substring_list:
        if int(substring) % 2 != 0:
            odd_count += 1
    return odd_count

print(return_odd_substrings_in_string('1357'))