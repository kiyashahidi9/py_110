'''
input: no input
output: a UUID

explicit rules:
- 8-4-4-4-12 character pattern
- it can have the digits 0-9, and the letters a-f
- each character has to be randomized between them

ALG:
1. specify the valid characters
2. create a list of 8 characters with each character 
    randomized between the valid characters
3. do the same for the rest of the character blocks
4. append the lists into a single string with a - separator
'''

import random as r

def gen_uuid():
    VALID_CHARS = 'abcdef0123456789'
    block1 = ''.join([r.choice(VALID_CHARS) for _ in range(8)])
    block2 = ''.join([r.choice(VALID_CHARS) for _ in range(4)])
    block3 = ''.join([r.choice(VALID_CHARS) for _ in range(4)])
    block4 = ''.join([r.choice(VALID_CHARS) for _ in range(4)])
    block5 = ''.join([r.choice(VALID_CHARS) for _ in range(12)])

    return f'{block1}-{block2}-{block3}-{block4}-{block5}'

print(gen_uuid())