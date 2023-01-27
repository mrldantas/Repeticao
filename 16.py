# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

ultimo = 1
penultimo = 1
numero = 0

while (numero < 500):
    numero = ultimo + penultimo
    penultimo = ultimo
    ultimo = numero
    if (numero < 500):
        print(numero)
    else:
        print("Próximo número é maior que 500")
