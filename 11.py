# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

# Altere o programa acima para mostrar no final a soma dos números.

primeiroNumero = int(input("Insira o primeiro número: "))
segundoNumero = int(input("Insira o segundo número: "))

soma = 0

if (primeiroNumero > segundoNumero):
    for i in range(segundoNumero + 1, primeiroNumero):
        print(i)
        soma = soma + i

elif (segundoNumero > primeiroNumero):
    for i in range(primeiroNumero + 1, segundoNumero):
        print(i)
        soma = soma + i

else:
    print("Os números são iguais")

print(f"A soma dos número é igual a: {soma}")
