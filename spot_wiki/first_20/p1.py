'''
input: string
output: a dictionary

explicit rules:
    - the dictionary should count the occurence of each lowercase letter
        keep track of them in the value

question:
    - what do i do with non lowercase letters?
        - the input is just lowercase letters
    - is there a particular order?
        - no

data structure:
    - a dictionary to keep track of letters

ALG:
1. take the string
1.. initialize an empty dictionary, `letter_count`
1... create a list of the lowercase characters
    - using a comprehension and selecting using the .islower() method
2. go through each letter in the list of lowercase characters
    - for loop
3. if the letter hasn't been encountered,
    - create a new key:value pair and begin the count at 1
4. if the letter has been encountered,
    - increment the value by 1
5. repeat 3 and 4 for each letter
6. return the dictionary

step 2 through 4
1. key reassignment using a .get method.
2. If the key doesn't exist, the default return value should be 0
    - a new key is created
3. add 1 to the .get() method
'''

def letter_count(string):
    letter_count_dict = {}
    lower_chars = [char for char in string if char.islower()]
    
    for char in lower_chars:
        letter_count_dict[char] = letter_count_dict.get(char, 0) + 1

    return letter_count_dict

print(letter_count('launchschool'))