'''
input: two strings
output: a boolean

rule
    - returns true
        - if every char in the second string occurs in the first string
        - character has to occur uniquely
    - otherwise, false
    - only lower case letters will be input

data structure
    - list to hold unused characters

ALG:
1. take scrambled_chars and word
2. split scrambled_chars into a list of characters
3. go through char in word,
    - if the char is in scrambled char, remove the first occurence of the char
    - if not, return false
4. return True if conditional goes through
'''
def scramble(scrambled_chars, word):
    scrambled_chars = list(scrambled_chars)
    for char in word:
        if char in scrambled_chars:
            scrambled_chars.remove(char)
        else:
            return False
    return True

print(scramble('rkqodlw', 'world')) # should return True
print(scramble('cedewaraarossoqqyt', 'carrot')) # should return True
print(scramble('katas', 'steak')) # should return False
print(scramble('scriptjava', 'javascript')) # should return True
print(scramble('scriptingjava', 'javascript')) # should return True