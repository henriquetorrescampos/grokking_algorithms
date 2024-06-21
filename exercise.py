#"Implemente um algoritmo para determinar se uma string não tem caracteres repetidos."

# def repetidos(string):
#     char_set = set() #retorna um conjunto com uniques numeros
#     for i in string:
#         if i in char_set:
#             return 'sou repetido'
#         else:
#             char_set.add(i)
#     return 'nao sou repetido'

# repetidos('string')
# repetidos('testa')

def has_unique_characters(s):
    # Ordena a string
    sorted_s = sorted(s)
    
    # Verifica caracteres adjacentes na string ordenada
    for i in range(1, len(sorted_s)): # 3 iterações
        if sorted_s[i] == sorted_s[i-1]:
            return 'sou repetido'
        
    return 'nao sou repetido'

has_unique_characters('tesa')