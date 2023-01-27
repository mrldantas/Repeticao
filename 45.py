# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
# o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por
# resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma

gabarito = []
respostasAlunos = []
notaFinal = []

nota = 0
continuar = True
aluno = 1
i = 0

print("\nInsira o gabarito: ")

for i in range(2):
    print(f"Questão: {i + 1}")
    respostaCorreta = gabarito.append(input("Insira a alternativa correta: "))

while (continuar != 'N'):
    print("\n")
    print(f"Aluno n° {aluno}:")
    respostasAlunos.clear()
    for i in range(2):
        print(f"Questão: {i + 1}")
        respostasAluno = respostasAlunos.append(input("Insira a alternativa: "))
    for i in range(2):
        if (respostasAlunos[i] == gabarito[i]):
            nota = nota + 1
    notaFinal.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [S/N] : ")
    aluno = aluno + 1

print(f"\nA maior nota tirada foi: {round(max(notaFinal) / len(notaFinal))}")
print(f"A menor nota tirada foi: {min(notaFinal) - 1}")
print(f"A media de notas da turma foi de: {(int(sum((notaFinal)) / len(notaFinal)) - 1)}")
