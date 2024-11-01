'''
input: a string
output: a new string

explicit rules:
    - every other character letter is capitalized
    - the first letter is capitalized
    - special characters cannot be capitalized, 
        - and do not count towards the stagger

implicit rules:
    - empty strings return empty strings

data structure:
- a list to contain the characters

ALG
1. take the string
2. split it into a list
3. capitalize every other character letter
4. return the joined list

step 3
1. take the list
2. capitalize the first character
3. for every character after,
    - determine if the character before it is a letter
    - if so, do the alternate of the current case
    - if not, don't do anything
    - move on to the next letter
'''

def find_previous_char_idx(string_list, current_char_idx):
    for idx in range(current_char_idx - 1, -1, -1):
        if string_list[idx].isalpha():
            return idx

def staggered_case(string):
    string_list = list(string.capitalize())

    for idx in range(1, len(string_list)):

        previous_char_idx = find_previous_char_idx(string_list, idx)

        if string_list[previous_char_idx].isupper():
            string_list[idx] = string_list[idx].lower()
        else:
            string_list[idx] = string_list[idx].upper()

    return ''.join(string_list)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

