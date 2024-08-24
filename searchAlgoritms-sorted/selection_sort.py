def selection_sort(my_list):
    lowest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < lowest:
            lowest = my_list[i]
    return lowest
    
print(selection_sort([9, 1, 5, 20, 10]))


def select_sort(array):
    array_len = len(array)

    for i in range(array_len - 1):
        lower_index = i
        for j in range(i + 1, array_len):
            if array[j] < array[lower_index]:
                lower_index = j
        
        array[i], array[lower_index] = array[lower_index], array[i]
    
    return array

array = [10, 20, 1, 2]
print(f'Sorted array: {select_sort(array)}')