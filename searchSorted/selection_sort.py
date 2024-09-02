def selection_sort(array):
    array_len = len(array)
#time O(n2), space O(1)
    for i in range(array_len - 1):
        lower_index = i
        for j in range(i + 1, array_len):
            if array[j] < array[lower_index]:
                lower_index = j
        
        array[i], array[lower_index] = array[lower_index], array[i]
    
    return array

array = [10, 20, 1, 2]
print(f'Sorted array: {selection_sort(array)}')

def lowest_num(my_list):
    lowest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < lowest:
            lowest = my_list[i]
    return lowest
    
print(lowest_num([9, 1, 5, 20, 10]))


#              0           1         2          3           4           5
intervals = [(8, 9), (11, 11.25), (9, 11), (11.5, 13), (10, 10.75), (8, 9)]
#             0, 1     0 , 1       0, 1      0,   1      0,   1      0,  1
intervals.sort(key=lambda x: x[0])

count = 1
end = intervals[0][1]

for interval in intervals[1:]:
    if interval[0] > end:
        end = interval[1]
        print(end)
        count += 1

print(count)