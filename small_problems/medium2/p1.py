'''
input: a string
output: a dictionary with 3 keys

rules:
    - the percentage of lowercase characters
    - the percentage of uppercase characters
    - the percentage of nonalpha characters
    - to get a percentage, you divide the amount of characters 
        by the total length of the string and multiply it by 100
    - each percentage should be properly formatted to 2 decimal places
    - there will always be at least one character
    - the values are strings

data structure:
    - an integer to keep track

ALG:
1. take the string
2. initialize a total_length variable
3. initialize 3 variables, 
    - upper_chars, lower_chars, and nonalpha_chars to 0
4. go through each character in the string
    - if the character is upper, increment upper_chars
    - do the same for the two other variables
5. initialize a dictionary
    - the keys will be 'lowercase', 'uppercase', 'neither'
    - the values will be the 3 counter variables 
        divided by the total_length, multiplied by 100
        - formatted to two decimal places
        - converted to a string
6. return the dictionary
'''

def letter_percentages(string):
    total_length = len(string)
    upper_chars, lower_chars, nonalpha_chars = (0, 0, 0)

    for char in string:
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1
        else:
            nonalpha_chars += 1

    percentage_dict = {
        'lowercase': f'{(lower_chars / total_length * 100):.2f}',
        'uppercase': f'{(upper_chars / total_length * 100):.2f}',
        'neither': f'{(nonalpha_chars / total_length * 100):.2f}'
    }
    
    return percentage_dict

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

