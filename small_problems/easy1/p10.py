'''
input: an integer
output: a string of that integer

rules:
    - not allowed to use str() function
    - extract the number from right to left
    - modulus dividing by 10 returns the leftmost number

data structure:
    - dictionary to hold int:string pairs
    - a list to hold the extracted numbers

ALG:
1. take the integer
2. create a dict of int:string pairs
3. initialize a list to hold numbers
4. extract the rightmost number by modulus dividing the integer by 10
5. capture that number in the list
6. repeat until the number is 
'''