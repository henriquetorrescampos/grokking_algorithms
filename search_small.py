def search_smaller(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i
    print(f'Smaller number {smaller}, smallar index {smaller_index}')
 
arr = [10, 16, 4, 5]

search_smaller(arr) 
