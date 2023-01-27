# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = int(input("Insira um número de 0 a 10: "))

while (numero < 0) or (numero > 10):
    numero = int(input("Insira um número válido: "))
    if ((numero > 0) and (numero <= 10)):
        print("Número Válido")
        exit()
