# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

termo = int(input("Insira qual termo deseja descobrir: "))
ultimo = 1
penultimo = 1

if ((termo == 1) or (termo == 2)):
    print("1")
else:
    count = 3
    while (count <= termo):
        numero = ultimo + penultimo
        penultimo = ultimo
        ultimo = numero
        count = count + 1
    print(numero)
