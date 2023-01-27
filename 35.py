# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista
# dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Insira até qual número você quer descobrir: '))

numeros = []
divisores = 0

for i in range(2, numero + 1):
    for count in numeros:
        if (i % count == 0):
            divisores = divisores + 1
    if (divisores == 0):
        numeros.append(i)
    divisores = 0

print(numeros)
