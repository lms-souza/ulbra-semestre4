# 1

numeros_pares = []

def soma_pares(lista):
    soma = 0
    global numeros_pares
    for item in lista:
        try:
            numero = float(item)
            if numero % 2 == 0:
                soma += numero
                numeros_pares.append(numero)
        except ValueError:
            print(f"valor inválido: {item}.")
    return "A soma dos pares é:" + str(soma)
    
entrada = input("Informe uma lista de numeros separados por virgula(,):\n").split(",")

resultado_soma = soma_pares(entrada)
print(resultado_soma)

# 2

def calculaImc(peso, altura):
    imc = peso / (altura **2)
    return imc

def indiceimc(imc):
    print("O seu IMC é:", imc)
    if imc <= 18.5:
        print("Você está abaixo do peso ideal!")
    elif imc >18.5 and imc < 24.9:
        print("Você está no peso ideal!") 
    elif imc >25.0 and imc < 29.9:
        print("Você está acima do peso ideal!")  
    elif imc >30.0 and imc < 34.9:
        print("Você está com obesidade grau I!") 
    elif imc >35.0 and imc < 39.9:
        print("Você está com obesidade grau II!") 
    elif imc >40.0:
        print("Você está com obesidade grau III!") 

peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite a sua altura (m):"))
imc_calculado = calculaImc(peso, altura)
indiceimc(imc_calculado)

# 3

def verifica_numeros(lista):
    maior = 0
    menor = float(lista[0])

    for item in lista:
        try:
            numero = float(item)
            if maior < numero:
                maior = numero
            elif menor > numero:
                menor = numero
        except ValueError:
            print(f"Valor invalido: {item}.")
    return (f"Maior Numero:{maior} | Menor Numero: {menor}")

entrada = input(f"Informe uma lista de numero separados por virgula(,):\n").split(",")

numeros_retornados = verifica_numeros(entrada)
print(numeros_retornados)

# 4

def conta_vogais(string):
    vogais = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count

entrada = input("Digite a palavra:")
resultado = conta_vogais(entrada)
print(f"A quantidade de vogais é: {resultado}")