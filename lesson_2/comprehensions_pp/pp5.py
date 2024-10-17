'''
ALG:
1. take the list of sublists
2. go through each list, find the sum of odd numbers
3. add the sum of odd numbers to a list
4. order the original list based on the sum of odd numbers
'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def find_odd_sum(sublist):
    return sum([num for num in sublist if num % 2 != 0])

ordered_lst = sorted(lst, key=find_odd_sum)

print(ordered_lst)