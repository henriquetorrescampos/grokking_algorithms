def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n - 1)
    
print(factorial2(5))


def add(n):
    if n <= 0: #base case
        return 0
    else: # 2 + add(1) / 
        return n + add(n - 1) #recusive case

add(2)