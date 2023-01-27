# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média
# dos votos restantes. Você deve fazer um programa que receba o nome do
# ginasta e as notas dos sete jurados alcançadas pelo atleta em sua
# apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média
# com as notas restantes). As notas não são informados ordenadas. Um
# exemplo de saída do programa deve ser conforme o exemplo abaixo:

notas = []
nome = True

while (nome != ''):
    print("\nPróximo atleta")
    nome = input("Digite o nome do atleta: ")
    if (nome == ''):
        break
    else:
        jurado = 1
        for i in range(7):
            print(f"Jurado n° {jurado}")
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            jurado = jurado + 1
        print(f"Atleta: {nome}")
        jurado = 1
        count = 0
        for i in range(7):
            print(f"{jurado}° Jurado: {notas[count]}")
            jurado = jurado + 1
            count = count + 1
        print("Resultado Final:")
        print(f"Nome do atleta: {nome}")
        print(f"Melhor nota: {max(notas)}")
        print(f"Pior nota: {min(notas)}")
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print(f"Media: {round(media)}")
