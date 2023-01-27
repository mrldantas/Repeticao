# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
# de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Insira a quantidade de turmas: "))

quantidadeAlunos = []
turma = 1

for i in range(turmas):
    alunos = int(input("Insira a quantidade de alunos por turma: "))
    while (alunos > 40):
        alunos = int(input("Insira a quantidade de alunos novamente: "))
    turma = turma + 1
    quantidadeAlunos.append(alunos)

media = sum(quantidadeAlunos) / len(quantidadeAlunos)
print(f"A média de alunos por turma é: {round(media)}")
