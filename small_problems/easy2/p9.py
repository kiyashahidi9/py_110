'''
input: a list of elements with some duplicates
output: lines of string with each element counted
rules:
    explicit:
        - case matters
        - keys must be counted
'''
'''
data structure:
- dictionary to keep count of elements
'''
'''
ALG
1. take the list
2. go through each element of the list
3. add new elements to a dictionary, if it already exists increment by 1
4. continue until you have a dictionary of element: occurence pairs
5. for each key:value pair, print out the formatted string
'''

def count_occurrences(lst):
    count_dict = {}
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1
    for key, value in count_dict.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)