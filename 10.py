# Faça um programa que receba dois números inteiros e gere os 
# números inteiros que estão no intervalo compreendido por eles.

primeiroNumero = int(input("Insira o primeiro número: "))
segundoNumero = int(input("Insira o segundo número: "))

while (primeiroNumero > segundoNumero):
    primeiroNumero = int(input("Insira o primeiro número: "))
    segundoNumero = int(input("Insira o segundo número: "))
else:
    for i in range(primeiroNumero + 1, segundoNumero):
        print(i)
