'''
input: a lowercase string
output: an integer

rules:
    - the integer should be the length of the longest chain of vowel substrings
    - if the current character is a vowel, and the previous character is a vowel
        - add to count
    - if the current character is not a vowel, count should reset
    - the longest count should be returned

data structure:
    - a list to keep track of the counts
    - an integer to keep count

ALG:
1. take the string
1.. initialize a count variable to 0
1... initialize a counts list to []
2. go through each character
3. if the current character is a vowel, add 1 to current count
4. if the current characer isn't a vowel,
    - add the current count to counts list
    - reset count to 0
5. repeat for each character
6. return the highest of the counts list
'''

def solve(string):
    current_count = 0
    counts = []
    VOWELS = 'aeiou'
    for char in string:
        if char in VOWELS:
            current_count += 1
        else:
            counts.append(current_count)
            current_count = 0
    return max(counts)

print(solve('suoidea'))