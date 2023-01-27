# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
# que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor
# e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []
tempInseridas = True

while (tempInseridas != 0):
    tempInseridas = (int(input("Insira a temperatura: ")))
    temperaturas.append(tempInseridas)

print(f"Menor temperatura: {min(temperaturas)}")
print(f"Maior temperatura: {max(temperaturas)}")
print(f"Média = {round(sum(temperaturas) / (len(temperaturas) - 1))}")
