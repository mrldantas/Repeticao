# Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número
# de divisões que ele executou para encontrar os números primos.

numero = int(input('Insira um número: '))

numeros = []
divisores = 0

for i in (range(2, numero + 1)):
    for count in numeros:
        if (i % count == 0):
            divisores = divisores + 1
    if (divisores == 0):
        numeros.append(i)
    divisores = 0

print(numeros)
print(len(numeros) * 2)
