'''
input: a list of directions n, s, e ,w
output: a boolean 

rules:
    - the walk needs to be a length of 10
    - you will need to end up where you started
    - the amount of norths should equal the amount of souths
    - the amount of wests should equal the amount of easts

data structure:
    - a dictionary initialized with n, s, e, w
        - to keep track of how many times each direction was went

ALG:
1. take the list
2. if length of list is not equal to 10, return false
2.. intialize a direction_dict
3. go through each direction in the list
    - increment the appropriate key by 1 for each direction
4. check if the values of n equal s, and w equal e
5. return if both conditions are true
'''

def is_valid_walk(direction_lst):
    if len(direction_lst) != 10:
        return False
    
    direction_dict = {
        'n': 0,
        's': 0,
        'e': 0,
        'w': 0,
    }
    for direction in direction_lst:
        direction_dict[direction] += 1

    return (direction_dict['n'] == direction_dict['s'] 
            and direction_dict['e'] == direction_dict['w'])

print(is_valid_walk(['n','s','n','s','n','s','n','s','w','s']))