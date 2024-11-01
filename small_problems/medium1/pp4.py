'''
A stack: a list of values that grows and shrinks dynamically
    - by appending and popping items from the topmost stack item

register: the current value

stack-and-register programming language: uses a stack instead of variables for all of its data
    - each operation operates on a register

an operation that requires two values 
    - pops the topmost item from the stack, 
    - operates on the popped value and the register value,
    - then stores the result back in the register

input: a series of strings with stack-and-reg commands
output: the register

rules:
    - stack and register are initialized to [] and 0
    - all programs provided to the function are valid
    - operations
        - n: place n in the register. do not modify stack
        - PUSH: push the current register value onto the stack. Leave the value in the reg
        - ADD: pop a value from the stack and add it to the register value, storing the result in the register
        - SUB: pop a value from the stack and subtract it from the register value, storing the result in the register
        - MULT: pop a value from the stack and mutliply from by the register value, storing result in reg
        - DIV: same as above but for //
        - REMAINDER: same as above but for %
        - POP: remove the topmost item from the stack and place it in the register
        - PRINT: print the register value

data structure
    - a list for the stack
    - an integer for the register
    - a list for the string
    - a match case for the commands

ALG:
1. intialize stack and register variables to [] and 0
1. take the string
2. split it into a command_list
3. iterate through each command in the list
4. with a match case statement, determine the command
5. perform the operation in the case statement
'''

def minilang(string):
    stack, register = ([], 0)
    command_list = string.split()

    for command in command_list:
        try:
            register = int(command)
        except ValueError:
            pass

        match command:
            case 'PRINT':
                print(register)
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'POP':
                register = stack.pop()
                
minilang('PRINT')
# # 0

minilang('5 PUSH 3 MULT PRINT')
# # 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

minilang('5 PUSH POP PRINT')
# # 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

