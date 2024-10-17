'''
input: two integers
    - a count 
    - the starting number of a sequence
output: a list

rules
    explicit:
        - the count is the amount of elements in the sequence
        - each number is the last number plus the starting number

data structures:
- a range to hold the count
- a list to hold the numbers

ALG:
1. take the count and the start_number
2. create a result list and add the start_number
3. iterate through a loop until the count using a range
    - a variable `idx` should reference the value of the current iteration
4. append a number which is the last number in the list plus the starting_number
5. return result list
'''

def sequence(count, start_number):
    result = [start_number]
    if count == 0:
        return []

    for idx in range(0, count - 1):
        result.append(result[idx] + start_number)
    return result

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True