'''
input: a list of integers
output: an integer

explicit rules:
    - the integer is a count of how many pairs in the list
    - a pair is two equal integers separated or not by other integers
    - whenever 2 of the same number occur, that is a pair
    - multiple pairs with the same number can occur
    - if the total amount of occurences is greater than 2, there is any number of pairs
        - total number // 2 to get the amount of pairs for that number

questions
1. how would we handle empty input?
    - we wouldn't expect that

data structures:
    - a dictionary to keep count of the occurence of each number

ALG:
1. take the list
1.. intialize an empty dictionary `count_nums`
1... initialize a pair_count integer to 0
2. count how many times each number occurs in a dictionary
3. go through each count
    - if its >= 2, add the value // 2 to pair_count
4. repeat for each count
5. return pair_count 

step 2.
1. iterate through the list with a for loop
2. key reassignment of the current char.
    - .get() method to get the value of the key and increment it by 1
    - the default value should be 0 if the key doesn't exist
    - a new key will be created
'''

def pairs(int_lst):
    count_nums = {}

    for num in int_lst:
        count_nums[num] = count_nums.get(num, 0) + 1
    
    pair_count = sum([count // 2 for count in count_nums.values() if count >= 2])
    
    return pair_count

print(pairs([1, 2, 5, 6, 5, 2]))
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))