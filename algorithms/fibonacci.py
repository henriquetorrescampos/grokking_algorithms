# 3 -> [1, 1, 2]
def fibonacci(num):
    if num < 0:
        raise Exception("The number needs to be positive.")

    res = [] # 1, 1
    prev, curr = 0, 1

    for i in range(num): # 5
        res.append(curr)
        curr, prev = curr + prev, curr 
        """
             
        curr = 1+0=1 e prev = 0 first loop
        curr = 1+1=2 e prev = 1 second loop
        curr = 2+1=3 e prev = 2 third loop
        curr = 3+2=5 e prev = 3 fourth loop
        curr = 5+3=8 e prev = 4 fifith loop

        
        """
    
    # exception negative number

    print(res)
    return res
    # return sequencie in a array

fibonacci(num=5)

"""
f(5) = f(4) + f(3) // 2 + 1
f(4) = f(3) + f(2) // 1 + 1
f(3) = f(2) + f(1) // 1 + 0

f(1)= 0, f(2)= 1, f(3)= 0+1=1, f(4)= 2
"""


def fibo(n):
    if n < 0:
        raise Exception('Precisa ser positivo')

    i, j = 0, 1
    #f(0)              f(1)
    numero_anterior, numero_atual = 0, 1

    for k in range(1, n):
        numero_atual, numero_anterior = numero_atual + numero_anterior, numero_atual
        t = i + j
        i = j
        j = t
        return i

print(fibo(num=5))