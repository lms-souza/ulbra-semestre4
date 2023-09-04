#Criar um algoritmo que gerencia uma fila com as seguintes funções:

def menu():
    print(
"""
1- ENFILEIRAR #ENQUEUE
2- DESENFILEIRAR #DEQUEUE
3- EXIBIR PRIMEIRO #FIRST
4- EXIBIR FILA
5- ENFILEIRAR PRIORITÁRIO
6- DESENFILEIRAR PRIORITÁRIO
7- EXIBIR PRIMEIRO PRIORITÁRIO
8- EXIBIR FILA PRIORITÁRIO
0- ENFILEIRAR #ENQUEUE

"""

    )

def enfileirar(lista,valor):
    lista.append(valor)

def desenfileirar(lista):
    if not lista:
        print("A lista está vazia!")
    else:
        lista.pop(0)

def exibir_primeiro(lista):
    if not lista:
        print("A lista esta vazia!")
    else:
        print(f"O primeiro elemento da lista é: {lista[0]}")

def exibir_fila(lista):
    if not lista:
        print("A lista está vazia!")
    else:
        for i in lista:
            print(i)

fila_prioritarios = []
fila = []

while True:

    menu()
    opc = int(input("Escolha uma opção:"))

    if opc == 1:
        valor = input("Digite um nome para colocar na fila:")
        enfileirar(fila, valor)
    elif opc == 2:
        desenfileirar(fila)
    
    elif opc == 3:
        exibir_primeiro(fila)

    elif opc == 4:
        exibir_fila(fila)
    elif opc == 5:
        valor = input("Digite um nome para colocar na fila:")
        enfileirar(fila_prioritarios, valor)
    elif opc == 6:
        desenfileirar(fila_prioritarios)
    elif opc == 7:
        exibir_primeiro(fila_prioritarios)
    elif opc == 8:
        exibir_fila(fila_prioritarios)
    elif opc == 0:
        break
    else:
        print("Escolha uma opção válida!")