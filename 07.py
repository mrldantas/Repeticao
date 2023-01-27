# Faça um programa que leia 5 números e informe o maior número.

numero = []
for num in range(1, 6):
    numero.append(int(input("Insira um número: ")))

maiorNumero = numero[0]

cont = 1
while (cont < len(numero)):
    if (numero[cont] > maiorNumero):
        maiorNumero = numero[cont]
    cont = cont + 1

print(f"O maior número é: {maiorNumero}")
