# 3 -> [1, 1, 2]
def fibonacci(num):
    if num < 0:
        raise Exception("The number needs to be positive.")

    res = [] # 1, 1
    prev, curr = 0, 1

    for i in range(num): # 5
        res.append(curr)
        curr, prev = curr + prev, curr # curr = 3+2 prev = 3, curr= 5+3 prev = 5
        # prev becames curr in the moment, not the result of curr
        # curr = curr + prev
    
    # exception negative number

    print(res)
    return res
    # return sequencie in a array

fibonacci(5)
fibonacci(0)
fibonacci(-5)