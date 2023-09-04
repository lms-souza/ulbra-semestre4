# Criar uma lista vazia para armazenar os números
numeros = []

# Criar uma lista vazia para armazenar os números removidos
removidos = []

# Criar uma função para validar a entrada do usuário
def validar_entrada(entrada):
  # Verificar se a entrada é uma string vazia
  if entrada == "":
    return False
  # Verificar se a entrada contém apenas números e vírgulas
  for caractere in entrada:
    if not (caractere.isdigit() or caractere == ","):
      return False
  # Verificar se a entrada não termina com uma vírgula
  if entrada[-1] == ",":
    return False
  # Verificar se a entrada não tem vírgulas consecutivas
  if ",," in entrada:
    return False
  # Se passar por todas as verificações, retornar True
  return True

# Criar um loop infinito para o menu
while True:
  # Mostrar as opções do menu
  print("Menu:")
  print("1- Adicionar números")
  print("2- Remover último")
  print("3- Limpar lista")
  print("4- Imprimir lista")
  print("5- Imprimir último")
  print("0- Sair")

  # Pedir ao usuário que escolha uma opção
  opcao = input("Escolha uma opção: ")

  # Verificar se a opção é válida
  if opcao in ["1", "2", "3", "4", "5", "0"]:
    # Converter a opção em um número inteiro
    opcao = int(opcao)

    # Executar a ação correspondente à opção escolhida
    if opcao == 1:
      # Pedir ao usuário que digite um número ou uma sequência de números separados por vírgula
      entrada = input("Digite um número ou uma sequência de números separados por vírgula: ")

      # Validar a entrada do usuário
      if validar_entrada(entrada):
        # Converter a entrada em uma lista de números inteiros
        numeros_entrada = [int(n) for n in entrada.split(",")]

        # Adicionar os números da entrada à lista de números
        numeros.extend(numeros_entrada)

        # Mostrar uma mensagem de sucesso
        print("Números adicionados com sucesso!")
      else:
        # Mostrar uma mensagem de erro
        print("Entrada inválida!")
    elif opcao == 2:
      # Verificar se a lista de números não está vazia
      if numeros:
        # Remover o último número da lista de números e armazená-lo na lista de removidos
        removidos.append(numeros.pop())

        # Mostrar uma mensagem de sucesso
        print("Último número removido com sucesso!")
      else:
        # Mostrar uma mensagem de erro
        print("A lista está vazia!")
    elif opcao == 3:
      # Limpar a lista de números e a lista de removidos
      numeros.clear()
      removidos.clear()

      # Mostrar uma mensagem de sucesso
      print("Lista limpa com sucesso!")
    elif opcao == 4:
      # Verificar se a lista de números não está vazia
      if numeros:
        # Imprimir a lista de números formatada como uma string separada por vírgulas
        print(f"Lista: {', '.join([str(n) for n in numeros])}")
      else:
        # Mostrar uma mensagem de erro
        print("A lista está vazia!")
    elif opcao == 5:
      # Verificar se a lista de números não está vazia
      if numeros:
        # Imprimir o último número da lista de números
        print(f"Último: {numeros[-1]}")
      else:
        # Mostrar uma mensagem de erro
        print("A lista está vazia!")
    elif opcao == 0:
      # Sair do loop e encerrar o programa
      break

    # Imprimir uma linha em branco para separar as interações do menu
    print()
  else:
    # Mostrar uma mensagem de erro se a opção não for válida
    print("Opção inválida!")