def menu():
    print(
"""
1- Adicionar no Início
2- Adicionar no final
3- Exibir Primeiro
4- Exibir Último
5- Remover Primeiro
6- Remover Último
0- Sair 

"""
    )

def adicionar_inicio(lista, valor):
    lista.insert(0, valor)

def adicionar_final(lista, valor):
    lista.append(valor)

def exibir_primeiro(lista):
    if not lista:
        print("O lista está vazio!")
    else:
        print(f"O primeiro elemento do lista é: {lista[0]}")

def exibir_ultimo(lista):
    if not lista:
        print("O lista está vazio!")
    else:
        print(f"O último elemento do lista é: {lista[-1]}")

def remover_primeiro(lista):
    if not lista:
        print("O lista está vazio!")
    else:
        valor = lista.pop(0)
        print(f"Removido o elemento: {valor}")

def remover_ultimo(lista):
    if not lista:
        print("O lista está vazio!")
    else:
        valor = lista.pop()
        print(f"Removido o elemento: {valor}")


lista = []

while True:
    menu()
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        valor = input("Digite um valor para adicionar no início: ")
        adicionar_inicio(lista, valor)
    elif opc == 2:
        valor = input("Digite um valor para adicionar no final: ")
        adicionar_final(lista, valor)
    elif opc == 3:
        exibir_primeiro(lista)
    elif opc == 4:
        exibir_ultimo(lista)
    elif opc == 5:
        remover_primeiro(lista)
    elif opc == 6:
        remover_ultimo(lista)
    elif opc == 0:
        break
    else:
        print("Escolha uma opção válida!")