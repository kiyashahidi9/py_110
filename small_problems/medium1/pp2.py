'''
input: an integer
output: an integer with max rotation

rules
    - first, rotate the leftmost digit
    - keep the first digit fixed in place
    - then, rotate the 2nd to left digit
    - keep the first two digits fixed in place
    - etc. etc

data structure:
    - for loop to iterate through the digits
    - our previous function

ALG:
1. take the number
2. convert it into a list
    - coerce into a string
3. for each element, perform the rightmost_digit rotation on it
4. return the joined list as an int
'''

def max_rotation(num):
    num_list = list(str(num))
    for idx in range(len(num_list)):
        rotate_rightmost_digits(num_list, len(num_list) - idx)
    
    return int(''.join(num_list))

def rotate_rightmost_digits(num_list, count):
    rotating_num = num_list.pop(len(num_list) - count)
    num_list.append(rotating_num)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True




