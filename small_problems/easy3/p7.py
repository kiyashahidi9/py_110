'''
input: a string with a first name, space, last name
output: another string: last name, comma, space, first name

data structures:
- a list to capture the elements

ALG:
1. take the name
2. split it into a list
3. return the last element, a comma and space, and the first element
    - f string
'''

def swap_name(name):
    list_name = name.split(' ')
    return f'{list_name[-1]}, {' '.join(list_name[0:-1])}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True