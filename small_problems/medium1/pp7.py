'''
input: a nth fibonacci number
output: the fibonacci number

rules
    - if n is less than or equal to two, the fibonacci number is 1
    - for each number, the last and second to last number are being added

data structure:
    - a list:
        - hold the values of the fibonacci sequence
        - return the last value

ALG:
1. we take the nth number
2. if the nth is less than or equal to 2, return 1
3. initialize nth to list [1, 1]
4. iterate through a range that goes from 2 to nth, 
5. for each iteration, add the last and the second to last numbers
6. append that value to the fibonacci list
7. return the last value of the list
'''

def fibonacci(nth):
    if nth <= 2:
        return 1
    fibonacci_list = [1, 1]

    for _ in range(2, nth):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list[-1]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True