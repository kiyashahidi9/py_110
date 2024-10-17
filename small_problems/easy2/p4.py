'''
ALGORITHM
1. take the list as a parameter
1. create a dictionary: 'count'
2. count the occurence of each number
3. return the value of the number with two occurences

step 2:
1. iterate through each object in the lst
2. create a new key for each object, add 1 if it already exists

step 3:
1. iterate through the key:value pairs
2. if the value is two, return the key
'''

def find_dup(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    for key, value in count.items():
        if value == 2:
            return key
        
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True


    