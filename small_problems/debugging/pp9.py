data_set = [1, 2, 3, 4, 5]
# new_set = {item for item in data_set if item % 2 != 0}
# print(new_set)

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)

print(data_set)