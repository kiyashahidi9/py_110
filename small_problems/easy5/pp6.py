'''
input: a list of integers
output: an integer
    - the sum of each leading subsequence

explicit rules:
    - the first number is summed
    - each segment is the next number plus the previous numbers

data structures:
- a list to hold the sub-sums

ALG
1. take the list
2. starting with the first number
3. go from the first number to each number after it to get a sub-sum
    - sum it and then return to a list
4. sum the list of sub-sums

step 2 and 3
1. iterate through a range equal to the length of the list
    - set current integer to 'idx'
2. add the first element to the element of the current index to a list
3. find the sum-sub of the list
4. return the list
'''

def sum_of_sums(lst):
    return sum([sum(lst[0:idx]) 
                for idx in range(1, len(lst) + 1)])

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True