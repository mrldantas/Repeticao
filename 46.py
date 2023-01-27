# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são 
# eliminados. O seu resultado fica sendo a média dos três valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
# pelo atleta em seus saltos e depois informe a média dos saltos conforme a 
# descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem 
# da execução, portanto não são ordenados. O programa deve ser encerrado quando não 
# for informado o nome do atleta.

nome = True
saltos = []
salto = 1
count = 0

while (nome != ''):
    print("\nPróximo atleta")
    nome = input("Insira o nome do atleta: ")
    if (nome == ''):
        break
    else:
        print("\n")
        for i in range(5):
            print(f"Salto n°{salto}")
            distancia_salto = float(input("Insira a distancia do salto: "))
            saltos.append(distancia_salto)
            salto = salto + 1
        print(f"\nAtleta: {nome}")
        salto = 1
        for i in range(5):
            print(f"{salto}° salto: {saltos[count]}m")
            salto = salto + 1
            count = count + 1
        print(f"\nMelhor salto: {max(saltos)}m")
        print(f"Pior salto: {min(saltos)}m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("\nMedia dos demais saltos: ", round(media, 2))
        print(f"\nResultado Final: \n{nome}: {round(media, 2)}")
