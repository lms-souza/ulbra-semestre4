import random
import time

def enfileirar (lista, valor):
    lista.append(valor)

def aleatorio(lista, valor):
    while len(lista) < valor:
        aleatorio = random.randint(1,10000)
        if aleatorio not in lista:
            enfileirar(lista, aleatorio)

def cronometro(algoritmo):
    inicio = time.time()
    algoritmo
    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo de processamento: {tempo:.8f} segundos. ")


def selection_sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
                
    return lista

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1, i,-1):
            if lista[j] < lista[j-1]:
                aux = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = aux
               # print(lista)
    return lista


lista_original = []

while True:
    print("""MENU:\n 1- Digitar número\n 2- Criar lista aleatória\n 3- Imprimir lista\n 4- Selection Sort\n 5- Bubble Sort\n 9-Limpar Lista\n 0- SAIR""")
    opc = int(input("Escolha uma opção:"))

    if opc == 0:
        break
    elif opc == 1:
        num = int(input("Digite um valor para Enfileirar: "))
        enfileirar(lista_original, num)
    elif opc == 2:
        valores = int(input("Escolha quantos elementos na lista:"))
        aleatorio(lista_original, valores)

    elif opc == 3:
        print(lista_original)
    
    elif opc == 4:
        cronometro(selection_sort(lista_original.copy()))
    elif opc == 5:
        cronometro(bubble_sort(lista_original.copy()))

    elif opc == 9:
        lista_original.clear()

    else:
        print("Escolha um valor no menu")