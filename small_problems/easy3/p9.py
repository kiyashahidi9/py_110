'''
input: a list of numbers from 0 to 19
output: a new list with the numbers sorted in order of their english words

data structure:
- a dictionary to keep track of english words

ALG:
1. take the numbers
2. sort them by the english word corresponding to that number

step 2.
1. take the number
2. match it to the appropriate value in a dictionary, return that value
3. sort using that value
'''

number_english = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

def alphabetic_number_sort(input_list):
    return sorted(input_list, key=num_to_english)

def num_to_english(num):
    return number_english[num]

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True