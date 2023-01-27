# Faça um programa que peça para n pessoas a sua idade, ao final o
# programa devera verificar se a média de idade da turma varia entre
# 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
# adulta ou idosa, conforme a média calculada.

termos = int(input("Insira a quantidade de termos: "))

todasIdades = []

for i in range(0, termos):
    notas = todasIdades.append(float(input("Insira um número: ")))
media = (sum(todasIdades) / termos)

if (0 < media <= 25):
    print(f"A turma é jovem, a media é {round(media)} anos")
elif (26 <= media < 60):
    print(f"A turma é adulta, a media é {round(media)} anos")
else:
    print(f"A turma é idosa, a media é {round(media)} anos")
