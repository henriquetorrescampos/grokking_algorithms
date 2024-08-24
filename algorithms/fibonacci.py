# 3 -> [1, 1, 2]
def fibonacci(num):
    if num < 0:
        raise Exception("The number needs to be positive.")

    res = [] # 1, 1
    prev, curr = 0, 1

    for i in range(num): # 5
        res.append(curr)
        curr, prev = curr + prev, curr 

    print(res)
    return res

fibonacci(num=5)
