## Questão 1
# # Implementação da classe Pilha usando lista
# class Pilha:
#     def __init__(self):
#         self.lista = [] # cria uma lista vazia
    
#     def push(self, elemento):
#         self.lista.append(elemento) # insere o elemento no final da lista
    
#     def pop(self):
#         return self.lista.pop() # remove e retorna o elemento do final da lista
    
#     def top(self):
#         return self.lista[-1] # retorna o elemento do final da lista sem remover

# # Implementação da classe Fila usando lista
# class Fila:
#     def __init__(self):
#         self.lista = [] # cria uma lista vazia
    
#     def enqueue(self, elemento):
#         self.lista.append(elemento) # insere o elemento no final da lista
    
#     def dequeue(self):
#         return self.lista.pop(0) # remove e retorna o elemento do início da lista
    
#     def front(self):
#         return self.lista[0] # retorna o elemento do início da lista sem remover

# # Cria uma pilha e uma fila vazias
# pilha = Pilha()
# fila = Fila()

# # Executa as operações do código original
# pilha.push('A')
# pilha.push('B')
# pilha.push('C')
# fila.enqueue(pilha.top())
# fila.enqueue(pilha.top())
# fila.enqueue('D')
# pilha.push(fila.dequeue())
# fila.enqueue(fila.dequeue())
# fila.enqueue(pilha.pop())
# pilha.push('E')
# fila.enqueue('E')
# pilha.pop()

# # Imprime o conteúdo da pilha e da fila
# print("Pilha:", pilha.lista)
# print("Fila:", fila.lista)

## Questão 2

# def recursao(n):
#     if n <= 10:
#         return n * 2
#     else:
#         return recursao(recursao(n // 3))

# n = 27
# resultado = recursao(n)
# print(resultado)

## Questão 3

