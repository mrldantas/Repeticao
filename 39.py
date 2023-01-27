# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
# o número do aluno e o segundo representando a sua altura em centímetros. Encontre
# o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número
# do aluno mais baixo, junto com suas alturas.

matricula = []
alturaAlunos = []

for i in range(10):
    numeroAluno = int(input("Insira sua matrícula: "))
    while numeroAluno in matricula:
        print("Esta matrícula já foi digitada")
        numeroAluno = int(input("Insira sua matrícula: "))
    alturaAluno = alturaAlunos.append(float(input("Insira sua altura: ")))
    matricula.append(numeroAluno)

baixo = alturaAlunos.index(min(alturaAlunos))
alto = alturaAlunos.index(max(alturaAlunos))

print(f"Aluno mais baixo: {matricula[baixo]} Altura: {int(min(alturaAlunos))}cm")
print(f"Aluno mais alto: {matricula[alto]} Altura: {int(max(alturaAlunos))}cm")
