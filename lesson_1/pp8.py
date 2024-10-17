statement = "The Flintstones Rock"
statement = statement.replace(' ', '')

frequency = {}

for char in statement:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
