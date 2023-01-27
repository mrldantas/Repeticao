# Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75]
# e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

numero = 1
conjunto1 = 0
conjunto2 = 0
conjunto3 = 0
conjunto4 = 0
conjunto5 = 0

while (numero > 0):
    numero = int(input("Insira um número: "))
    if ((numero >= 0) and (numero <= 25)):
        conjunto1 = conjunto1 + 1
    elif ((numero >= 26) and (numero <= 50)):
        conjunto2 = conjunto2 + 1
    elif ((numero >= 51) and (numero <= 75)):
        conjunto3 = conjunto3 + 1
    elif ((numero >= 76) and (numero <= 100)):
        conjunto4 = conjunto4 + 1
    elif ((numero > 0) and (numero > 100)):
        conjunto5 = conjunto5 + 1

print(f"Quantidade de números entre [0-25]: {conjunto1}")
print(f"Quantidade de números entre [26-50]: {conjunto2}")
print(f"Quantidade de números entre [51-75]: {conjunto3}")
print(f"Quantidade de números entre [76-100]: {conjunto4}")
print(f"Quantidade de números entre [101-...]: {conjunto5}")
