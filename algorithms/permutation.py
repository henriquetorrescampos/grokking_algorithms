def permutations(array):
    c = [0] * len(array)
    print(array)

    i = 0
    while i < len(array):
        if c[i] < i:
            if i % 2 == 0:
                array[0], array[i] = array[i], array[0]
            else:
                array[c[i]], array[i] = array[i], array[c[i]]
            print(array)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

array = [1, 2, 3]
permutations(array)