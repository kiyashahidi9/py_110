'''
input: a list of numbers
output: a different list of numbers
rules:
    explicit:
        - there are the same amount of elements in both lists
    implicit:
        - all elements are integers
        - each number is equal to itself plus the last number
        - the first number of each list always equals itself

questions:
1. are they the same list object?
'''
'''
data structure:
a list
iterate through the list

Algorithm:
1. create a new `result` list object
2. create a `running total` variable initialized to 0
2. go through the list and add to the running total
3. return the result list

step 2
1. iterate through the list elements
2. for each object, add the current number to the `running total`
3. append the running total to the result list
'''

def running_total(num_list):
    result_list = []
    current_total = 0
    for num in num_list:
        current_total += num
        result_list.append(current_total)
    
    return result_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
