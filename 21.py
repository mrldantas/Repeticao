# Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

numero = int(input("Insira o número: "))

if ((numero % 2 != 0) or (numero == 2)):
    print("O número é primo")
else:
    print("O número não é primo")
