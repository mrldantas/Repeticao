# Altere o programa de cálculo do fatorial (17), permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

numero = int(input("Insira o número que quer fatorar: "))

multiplicacao = 1

for i in range(1, numero + 1):
    multiplicacao = multiplicacao * i
    while ((numero // 1 != numero) or (numero < 0) or (numero > 16)):
        numero = float(input("Insira um número menor que 16: "))
        multiplicacao = multiplicacao * i

print(f"O resultado é: {multiplicacao}")
