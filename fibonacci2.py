# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))

def fa(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

print(fa(5))