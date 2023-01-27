# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

i = 1
par = 0
impar = 0

while (i <= 10):
    numero = int(input("Insira um número: "))
    i = i + 1
    if (numero % 2 == 0):
        numero = par
        par = par + 1
    else:
        numero = impar
        impar = impar + 1

print(f"Números pares: {par} e Números ímpares: {impar}")
