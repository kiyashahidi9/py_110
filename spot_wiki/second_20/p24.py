'''
input: a string
output: the string as a hashtag

rules:
    - every word is title case
    - no spaces between words
    - begins with a hashtag
    - return False
        - if length of string is more than 140
        - if string is empty
    - each word should be stripped of extra whitespace

Data structure:
    - a list of words

ALG:
1. take the string
1.. strip each word of whitespace
2. if string is empty, or length is more than 140
    - return False
3. split the string into a list of words
    - with every word capitalized
    - use a comprehension
4. return a hashtag with the list joined by an empty string
'''

def generate_hashtag(string):
    string = ' '.join(string.split())
    if string == '' or len(string) >= 140:
        return False
    word_list = [word.capitalize() for word in string.split()]
    return f'#{''.join(word_list)}'

print(generate_hashtag(""))                       # should return `False`
print(generate_hashtag(" " * 200))                # should return `False`
print(generate_hashtag("Do We have A Hashtag"))   # should return "#DoWeHaveAHashtag"
print(generate_hashtag("Nice To Meet You"))       # should return "#NiceToMeetYou"
print(generate_hashtag("this is a test"))         # should return "#ThisIsATest"
print(generate_hashtag("this is a very long string" + " " * 140 + "end"))  # should return "#ThisIsAVeryLongStringEnd"
print(generate_hashtag("a" * 139))                # should return "#A" + "a" * 138
print(generate_hashtag("a" * 140))                # should return `False`