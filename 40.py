# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

codigoCidade = []
veiculosClientes = []
acidentesVitimas = []
acidentes2000 = []

for i in range(2):
    print(f"\nCidade número {i + 1}")
    codigo = int(input("Insira o código da cidade: "))
    while codigo in codigoCidade:
        print("Este código já foi digitado")
        codigo = int(input("Insira o código: "))
    veiculos = int(input("Insira o número de carros de passeio: "))
    acidentes = int(input("Insira o número de acidentes com vítimas: "))
    if (veiculos <= 2000):
        acidentes2000.append(acidentes)
        acidentesVitimas.append(acidentes)
    else:
        acidentesVitimas.append(acidentes)
    codigoCidade.append(codigo)
    veiculosClientes.append(veiculos)

codigoAcidenteMin = acidentesVitimas.index(min(acidentesVitimas))
codigoAcidenteMax = acidentesVitimas.index(max(acidentesVitimas))

print(f"Menor índice de acidentes: {codigoCidade[codigoAcidenteMin]}")
print(f"Maior índice de acidentes: {codigoCidade[codigoAcidenteMax]}")
print(f"Média de veículos nas 5 cidades: {round(sum(veiculosClientes) / len(veiculosClientes))}")

if (veiculos >= 2001):
    print("Não houveram cidades com menos de 2000 veiculos")
else:
    mediaAcidentes2000 = (sum(acidentes2000) / len(acidentes2000))
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {mediaAcidentes2000}")
