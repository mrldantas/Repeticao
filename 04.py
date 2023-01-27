# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
# número de anos necessários para que a população do país A ultrapasse ou iguale 
# a população do país B, mantidas as taxas de crescimento.

primeiraPopulacao = 80000
segundaPopulacao = 200000
anos = 0

crescimentoA = 0.03
crescimentoB = 0.015

while (primeiraPopulacao < segundaPopulacao):
    anos += 1
    primeiraPopulacao = primeiraPopulacao + (primeiraPopulacao * crescimentoA)
    segundaPopulacao = segundaPopulacao + (segundaPopulacao * crescimentoB)


if (primeiraPopulacao >= segundaPopulacao):
    print(f"A população A vai ultrapassar ou igualar em {anos} anos")
    print(f"População A: {round(primeiraPopulacao)} habitantes")
    print(f"População B: {round(segundaPopulacao)} habitantes")
    exit()
