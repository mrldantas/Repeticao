#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes
# dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

valor = float(input("Insira o valor da dívida: "))
parcelas = 1
juros = 0

print("|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas|Valor da Parcela|")

while True:
    juros = (5 / 3) * parcelas + 5
    if (parcelas == 1):
        juros = 0
    valorJuros = valor * (juros / 100)
    valorTotal = valor + valorJuros
    valorParcela = valorTotal / parcelas
    print(
        f"|R$ {valorTotal:.2f}\t"
        f"|R$ {valorJuros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valorParcela:.2f}"
    )
    if (parcelas == 1):
        parcelas = parcelas - 1
    parcelas = parcelas + 3
    if (parcelas > 12):
        break
