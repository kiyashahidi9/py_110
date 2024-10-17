'''
ALG:
1. take the list
2. go through each sublist and order it
3. add the ordered sublist to a new list
4. return the new list
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

ordered_lst = [sorted(sublist) for sublist in lst]

print(ordered_lst)