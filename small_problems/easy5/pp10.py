'''
input: a list integers with duplicates
output: a new list

explicit rules
    - all duplicate items are removed
    - a different list is returned
    - order is maintained

data structure
    - we cannot use a set, it does not maintain order
    - for loop and in keyword

ALG
1. take the list
2. initialize a result list
2. if the number is not in original list, append to result list
3. return result list
'''

def unique_sequence(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

original = []
expected = []
print(unique_sequence(original) == expected)      # True