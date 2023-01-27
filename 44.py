# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

numerosElegiveis = [1, 2, 3, 4, 5, 6]
votos = []
voto = True

while (voto != 0):
    voto = (int(input("Qual candidato deseja votar? [1, 2, 3, 4, 5 ou 6]: ")))
    if (voto == 0):
        break
    else:
        while voto not in numerosElegiveis:
            voto = (int(input("Insira um número válido [1, 2, 3, 4, 5 ou 6]: ")))
        votos.append(voto)

nulo = (votos.count(5) / len(votos)) * 100
branco = (votos.count(6) / len(votos)) * 100

print("\n")
print(f"Votos para candidato 1: {votos.count(1)}")
print(f"Votos para candidato 2: {votos.count(2)}")
print(f"Votos para candidato 3: {votos.count(3)}")
print(f"Votos para candidato 4: {votos.count(4)}")
print(f"Votos Nulos: {votos.count(5)}")
print(f"Porcentagem Nulos: {int(round(nulo))}%")
print(f"Votos Brancos: {votos.count(6)}")
print(f"Porcentagem Brancos: {int(round(branco))}%")
