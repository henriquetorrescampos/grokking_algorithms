"""Bubble sort in O(n**2 way)"""

def bubble_sort(my_list):
    list_len = len(my_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1] , my_list[j] # swap

my_list = [9, 5, 4, 3, 1]
bubble_sort(my_list)
print(my_list)
