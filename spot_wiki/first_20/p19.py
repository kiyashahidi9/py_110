'''
input: a string, a string with exception words
output: a string thats title case

rules:
    - The first word should be titled, even if in the list of exceptions
    - every character should be title case, except if in the list of exceptions
    - the list of exceptions should disregard case

Data structure
    - a list

ALG:
1. take the string, string_exceptions
2. split both into a list, casefolding each word
3. go through the list words and their indexes, 
    - if the word is not in string_exceptions list,
        - mutate that index by making it title case
    - if it is
        - dont do anything
4. return the word list joined by whitespace
'''

def title_case(string, string_exceptions=''):
    string_list = [word.casefold() for word in string.split()]
    string_exceptions_list = [exception.casefold() 
                              for exception in 
                              string_exceptions.split()]
    
    string_list[0] = string_list[0].title()

    for idx, word in enumerate(string_list):
        if word not in string_exceptions_list:
            string_list[idx] = word.title()
    
    return ' '.join(string_list)

print(title_case('a Clash OF KINGS', 'a of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return 'The Wind in the Willows'
print(title_case('the quick brown fox'))