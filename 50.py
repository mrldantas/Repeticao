# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

numero = int(input("Digite o numero de termos: "))
primeiro = 1
segundo = 2
lista1 = []
lista2 = []

print("H = 1 + ", end="")

for i in range(1, numero - 1):
    print(f"{primeiro}/{segundo} + ", end="")
    lista1.append(primeiro)
    lista2.append(segundo)
    segundo = segundo + 1

print(f"{primeiro}/{segundo}")
print(f"Resultado da soma é: {sum(lista1) + 2}/{sum(lista2) + segundo}")
