def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    print(result)

n = 5

factorial(n)
