def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    lst_substrings = [leading_substrings(string[idx:]) for idx in range(len(string))]
    return [element for sublist in lst_substrings
                    for element in sublist]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True