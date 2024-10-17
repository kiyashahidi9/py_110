dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

'''
input: a dictionary
output: a list

explicit rules:
    - if the type is a fruit, we get the color values
        - the colors should be uppercase
    - if the type is a vegetable, we get the size value
        - the size should be capitalized

ALGORITHM:
1. go through the value of each key
2. if the type is fruit, add the colors to the list
    - capitalize each element of the colors list
3. if the type is vegetable, add the size to the list
    - make the size uppercase
'''

def filtered_return(subdict):
    if subdict['type'] == 'fruit':
        return [color.capitalize() for color in subdict['colors']]
    else:
        return subdict['size'].upper()

lst = [filtered_return(subdict) for subdict in dict1.values()]

print(lst)