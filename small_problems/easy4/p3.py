'''
input: a dictionary
output: a list of keys

explicit rules:
    - the keys are ordered based on their value

ALG:
1. take the dictionary
2. add the key, value pairs to a list
3. sort the list based on the second item in each tuple
4. return a list with the letters of the sorted list

step 3

'''

def order_by_value(dictionary):
    lst = sorted([(value, key) for key, value in dictionary.items()])
    return [tup[1] for tup in lst]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True