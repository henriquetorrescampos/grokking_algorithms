# Time: O(n)  Space: O(1)
def reverse(array):
    len_array = len(array)
    for i in range(len_array // 2):
        array[i], array[len_array -1 - i] = array[len_array - 1 - i], array[i]
    return array

array = [1, 2, 3, 4]

reverse(array)

''' 
Se iterarmos por toda comprimento da lista vamos acabar retornando a lista original.
Quando dividimos por 2 asseguramos que o loop irá iterar até a metade da lista
Ao trocarmos os elementos das extremidads indo ao centro garantimos a passagem em toda lista
'''

