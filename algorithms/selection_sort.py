def selection_sort(my_list):
    list_len = len(my_list)
    for i in range(list_len - 1):
        lowest = my_list[i] # the value
        index = i # the position
        for j in range(i + 1, list_len): #complexity of O(n**2)
            if my_list[j] < lowest:
                index = j
                lowest = my_list[j]
        my_list[i], my_list[index] = my_list[index], my_list[i]
        return lowest, my_list
    
print(selection_sort([9, 1, 5, 20, 10]))