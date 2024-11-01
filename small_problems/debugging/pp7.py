def sum_(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_(numbers, 2) == 20)