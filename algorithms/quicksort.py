def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        low = [i for i in array[1:] if i <= pivot] # list comprehension
        high = [i for i in array[1:] if i > pivot] # list comprehension
        return quicksort(low) + [pivot] + quicksort(high) # recursive case when call the function itself
    
print(quicksort([2, 5, 4, 1, 3]))
print(quicksort([3, 1]))
print(quicksort([2, 5, 4, 10]))

