'''
input: an integer
output: an integer
    - minus one digit

explicit rules
    - delete one digit from the input number
    - the returned integer should be the highest number of 
        all of the possible numbers when a digit is removed

data structure:
- a list to hold the possible choices

ALG:
1. take the integer
2. collect all of the possible numbers where a digit is removed into a list
3. return the highest number of that list

step 2:
input: an integer
output: a list of integers with each digit removed

ALG:
1. take the integer
2. convert it to a string and assign to `original_number`
3. iterate through a range of the length of `original_number` and assign current idx
4. add the original_number with the current idx ommited
5. return the list
'''

def list_deleted_digits(integer):
    original_number = list(str(integer))
    deleted_list = []
    for deleted_idx in range(len(original_number)):
        modified_number = original_number
    return original_number

print(list_deleted_digits(567))