'''
input: a string of a URL
output: a string of the domain

rules:
    - the domain is always before .com
    - always after //
    - there is potentially a www. before it

data structure:

ALG:
# 1. take the string
# 1.. initialize cleaned_word
# 2. find the occurence of .com
# 3. take the substring before .com and add to cleaned_word
4. find the occurence of //
5. take the substring after two indexes of //, reassign to cleaned_word
6. if cleaned_word begins with www., return cleaned word after 4th index
7. if not, return cleaned_word
'''

def domain_name(string):
    cleaned_word = ''
    cleaned_word = string[:string.find('.com')]
    cleaned_word = cleaned_word[cleaned_word.find('//') + 2:]
    if cleaned_word.startswith('www.'):
        return cleaned_word[4:]
    return cleaned_word

print(domain_name("https://cnet.com"))