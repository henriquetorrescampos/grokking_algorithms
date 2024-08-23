def binary_search(a_list, item):
    low = 0
    high = len(a_list) - 1 # binary search, starts with 0, that's why we have -1. 

    while low <= high:
        midle = (low + high) // 2 
        bet = a_list[midle]  
        
        if bet == item:  
           return midle
        elif bet > item: 
            high = midle - 1
        else:
            low = midle + 1  
    return None

num_list = [1, 3, 4, 5, 6]

print(binary_search(num_list, 6))

'''
Space Complexity
reflects aditional memory to run the algorithm
in this algorithm we have O(1) space complexity
because all the variable are O(1)
'''