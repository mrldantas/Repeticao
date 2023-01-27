eleitores = int(input("Insira o número de eleitores: "))

votos = []

for i in range(eleitores):
    voto = votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

print(f"Votos para candidato 1: {votos.count(1)}")
print(f"Votos para candidato 2: {votos.count(2)}")
print(f"Votos para candidato 3: {votos.count(3)}")
