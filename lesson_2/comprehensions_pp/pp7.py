lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def is_multiple_3(sublist):
    return [num for num in sublist if num % 3 == 0]

cleaned_lst = [is_multiple_3(sublist) for sublist in lst]

print(cleaned_lst)