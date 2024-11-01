'''
input: a string with WUB in between its words
output: a string without the WUBS

rules:
    - all WUBS must be removed
    - there may be more than one WUB in between each word

ALG:
1. take the string
2. while there are wubs in the string
3. replace WUB with a space
4. split the words into a list
5. strip each word of extra whitespace and join them with a single whitespace
'''

def song_decoder(string):
    while 'WUB' in string:
        string = string.replace('WUB', ' ')

    cleaned_string = return_extra_whitespace_removed(string)

    return cleaned_string

def return_extra_whitespace_removed(string):
    string_list = string.split()
    return ' '.join(string_list)

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))