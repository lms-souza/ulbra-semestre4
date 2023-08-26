lista = []

while True:

    print("Menu:\n 1- Adiona Valor\n 2- Remove Último\n 3- Limpa Lista\n 0- Sair")
    opc = int(input("Informe os valores:"))

    if opc == 1:
        entrada = input("Informe os valores: ")
        entrada_tratada = entrada.split(",")
        for i in entrada_tratada:
            try:
                num = int(i)
                lista.append(num)
            except ValueError:
                print(f"Valor {i} inválido")
            print(lista)
    
    elif opc == 2:
        lista.pop()
    elif opc == 3:
        lista.clear()
    elif opc == 4:
        print(lista)
    elif opc == 5:
        print(lista[-1])
    elif opc == 0:
        break
    else:
        print("Digite uma opção válida")
