'''
input: a positive integer
output: a true or false
    - if it is prime or not

rules:
    - A prime number is a positive number that is not evenly divisible by any number > 1 and < itself
    - number 1 is not prime

data structure:
    - a range

ALG:
1. take the num
6. if the number is 1, it is not prime
2. iterate through each number between 1 and the num
3. try to evenly divide the num by each number
4. if any of the divisions are even, the number is not prime
5. if not, the number is prime
'''

def is_prime(main_num):
    if main_num == 1:
        return False
    
    for num in range(2, main_num):
        if main_num % num == 0:
            return False
        
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True