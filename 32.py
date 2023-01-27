# Faça um programa que calcule o fatorial de um número inteiro fornecido
# pelo usuário. Ex.: 5!=5.4.3.2.1=120.

numero = int(input("Insira o número que quer fatorar: "))
count = numero
multiplicacao = 1

print(f"Fatorial de {numero}")

for i in range(2, numero + 1):
    multiplicacao = multiplicacao * i
    print(count, end=" * ")
    count = count - 1

print(f"1 = {multiplicacao}")
