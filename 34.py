# Os números primos possuem várias aplicações dentro da Computação, por exemplo
# na Criptografia. Um número primo é aquele que é divisível apenas por um e por
# ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
# ou não um número primo

numero = int(input("Insira o número: "))

if ((numero % 2 != 0) or (numero == 2)):
    print("O número é primo!")
else:
    print("O número não é primo!")
