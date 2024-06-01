a_list = [1, 1, 1, 1, 2, 2, 3, 4, 5]

new_list = {i: a_list.count(i) for i in set(a_list)}

print(new_list)