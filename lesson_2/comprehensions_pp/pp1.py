'''
input: a dictionary with nested info dicts
output: the total age of male family memebers

explicit rules:
    - the gender must be male
    - the ages are summed

Data structure:
- a list to hold the appropriate ages

ALG:
- filter through the correct ages and add to a list
- sum the list
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# result = []
# for info in munsters.values():
#     if info['gender'] == 'male':
#         result.append(info['age'])

# total_age = sum(result)
# print(total_age)

total_male_age = sum([info['age'] for info in munsters.values() 
                      if info['gender'] == 'male'])

print(total_male_age)