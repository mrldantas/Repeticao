# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

# Cópia do exercício 49

numero = int(input("Insira a quantidade de termos que quer descobrir: "))

primeiro = 1
segundo = 1
lista1 = []
lista2 = []

print("S = ", end="")

for i in range(1, numero):
    print(f"{primeiro}/{segundo} + ", end="")
    lista1.append(primeiro)
    lista2.append(segundo)
    primeiro = primeiro + 1
    segundo = segundo + 2

print(f"{primeiro}/{segundo}")
print(f"A soma é igual a: {sum(lista1)}/{sum(lista2)}")
