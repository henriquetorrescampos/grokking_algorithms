class Node:
    def __init__(self, value):
        self.value = value #self, ojeto que estamos criando; value, valor ou dado
        self.next = None # inicialmente, próximo nó é None, nó tem um lugar onde podemos conectar outro nó

class LinkedList: #criando uma nova classe
    def __init__(self):
        self.head = None #lista começa vazia, não aponta para nenhum nó
    # add novo nó no final da lista
    def append(self, value): 
        new_node = Node(value) #criando nova instância da classe. Novo nó com dado que recebemos
        if self.head is None: #se a lista está vazia não tem head
            self.head = new_node #novo nó se torna a cabeça da lista
            return #saímos da função pois adicionamos o nó
        last = self.head #começamos na cabeça da lista
        while last.next: #enquanto houver um próximo nó
            last = last.next #vamos para o proximo nó
        last.next = new_node # quando chegar ao fim conectamos novo nó
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
