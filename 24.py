# Faça um programa que calcule o mostre a média aritmética de N notas.

termos = int(input("Insira a quantidade de termos: "))

todasNotas = []

for i in range(0, termos):
    notas = todasNotas.append(float(input("Insira um número: ")))
print(sum(todasNotas) / termos)
