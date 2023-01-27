# Faça um programa que, dado um conjunto de N números, determine
# o menor valor, o maior valor e a soma dos valores.

termos = int(input("Insira a quantidade de termos: "))

menor = 0
maior = 0

for i in range(0, termos):
    numero = int(input("Insira um número: "))
    if (menor == 0 or numero < menor):
        menor = numero
    if (numero > maior):
        maior = numero

print(f"Menor é: {menor}")
print(f"Maior é: {maior}")
print(f"Soma é igual a: {menor + maior}")
