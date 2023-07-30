import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

one_hot_data = []
unique_values = list(set(lst))

for value in lst:
    one_hot_encoding = {f'whoAmI_{value}': 1 if value == item else 0 for item in unique_values}
    one_hot_data.append(one_hot_encoding)

one_hot_data = []
for value in lst:
    one_hot_encoding = {}
    for item in unique_values:
        if value == item:
            one_hot_encoding[f'whoAmI_{item}'] = 1
        else:
            one_hot_encoding[f'whoAmI_{item}'] = 0
    one_hot_data.append(one_hot_encoding)

for row in one_hot_data[:5]:
    print(row)