lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_num(subdict):
    return {key: num + 1 for key, num in subdict.items()}

incremented_lst = [increment_num(subdict) for subdict in lst]

print(incremented_lst)