# string = 'testando'
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

def permutation(array, n):
    if n == 1:
        print(array)
        return 
    
    for i in range(n):
        permutation(array, n - 1)
        if n % 2 == 0:
            array[i], array[n-1] = array[n-1], array[i]
        else:
            array[0], array[n-1] = array[n-1], array[0]
    return array

array = [1, 2, 3]

permutation(array, len(array))