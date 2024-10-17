'''
input: two lists
output: one list
    - each element is multiplied by the other
'''
'''
ALGORITHM
1. take the two lists
1. initialize `result` empty list
2. pack them in a list of tuples
3. assign that to a `zipped_num` variable
4. multiply each tuple by eachother
5. append that to a `result` list
6. repeat step 4 and 5 until all tuples are multiplied
7. return result list
'''

def multiply_list(lst1, lst2):
    result = []
    for num1, num2 in zip(lst1, lst2):
        result.append(num1 * num2)
    return result

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True