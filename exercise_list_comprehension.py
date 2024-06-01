from collections import Counter

a_list = [1, 1, 1, 1, 2, 2, 3, 4, 5]

new_list = {i: a_list.count(i) for i in set(a_list)}

print(new_list)

# ----- 

list_to_dict = {}

for number in a_list:
    if number in list_to_dict:
        list_to_dict[number] += 1
    else:
        list_to_dict[number] = 1

print(list_to_dict)

# ------

counts = Counter(a_list)
counts_dict = dict(counts)
print(counts_dict)