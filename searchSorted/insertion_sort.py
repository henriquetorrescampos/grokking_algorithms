#time O(n2) space O(1)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        number_to_order = my_list[i] 
        j = i - 1
        while j >= 0 and number_to_order < my_list[j]: 
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = number_to_order
    return my_list

print(insertion_sort([10, 1, 4, 5, 6, 7]))