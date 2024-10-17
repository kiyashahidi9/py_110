'''
input: two lists
output: one list
    - elements from two lists interleaved
rules:
    explicit:
        - the elements are still in order
'''


def interleave(lst1, lst2):
    result = []
    zipped_list = zip(lst1, lst2)
    for e1, e2 in zipped_list:
        result.extend([e1, e2])
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True