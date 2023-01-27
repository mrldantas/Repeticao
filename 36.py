# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que
# será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar
# em 1 e terminar em 10, o valor inicial e final devem ser informados também
# pelo usuário, conforme exemplo abaixo:

numero = int(input("Insira qual tabuada você quer ver: "))
primeiroNumero = int(input("Insira o multiplicador inicial: "))
segundoNumero = int(input("Insira o multiplicador final: "))

while (primeiroNumero > segundoNumero):
    segundoNumero = int(input("Insira o multiplicador final (primeiro < segundo): "))

print(f"Montar tabuado do: {numero}")
print(f"Começar por: {primeiroNumero}")
print(f"Terminar em: {segundoNumero}")

for i in range(primeiroNumero, segundoNumero + 1):
    print(f"{numero} X {i} = {numero * i}")
