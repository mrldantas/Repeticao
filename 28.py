# Faça um programa que calcule o valor total investido por um colecionador
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário
# deverá informar a quantidade de CDs e o valor para em cada um.

CDs = int(input("Insira a quantidade de CDs: "))

quantidadeCDs = []
CD = 1

for i in range(CDs):
    valorCD = int(input("Insira o valor de cada CD:  "))
    CD = CD + 1
    quantidadeCDs.append(valorCD)

media = sum(quantidadeCDs) / len(quantidadeCDs)
print(f"O valor médio de cada CD é: {round(media)} reais")
