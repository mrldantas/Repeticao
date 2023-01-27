# Altere o programa de cálculo dos números primos, informando,
# caso o número não seja primo, por quais número ele é divisível.

numero = int(input("Insira um número: "))

divisiveis = []

if ((numero % 2 != 0) or (numero == 2)):
    print("O número é primo")
    exit()
else:
    for i in range(numero):
        if ((numero % (i + 1)) == 0):
            divisiveis.append(i + 1)

print("O número não é primo")
print(f"É divisível por: {divisiveis}")
