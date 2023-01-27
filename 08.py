# Faça um programa que leia 5 números e informe a soma e a média dos números.

numero = []
for num in range(1, 6):
    numero.append(int(input("Insira um número: ")))

print(f"A soma é igual a: {sum(numero)}")
print(f"A média é igual a: {sum(numero)/(len(numero))}")
