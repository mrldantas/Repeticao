# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães,
# de 1 até 50 pães, a partir do preço do pão informado pelo usuário.

produtos = int(input("Insira a quantidade de produtos: "))
preco = produtos * 0.18

print("Lojas Quase Dois - Tabela de preços")

while (0 < produtos > 51):
    produtos = int(input("Insira a quantidade de produtos (máximo 50): "))

print(f"Quantidade de produtos: {produtos}")
print(f"Preço total da compra: {round(preco)} reais")
