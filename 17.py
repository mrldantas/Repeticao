# Faça um programa que calcule o fatorial de um número 
# inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Insira o número que quer fatorar: "))

multiplicacao = 1

for i in range(1, numero + 1):
    multiplicacao = multiplicacao * i

print(f"O resultado é: {multiplicacao}")
