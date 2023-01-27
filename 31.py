# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
# agora possui uma loja de conveniências. Faça um programa que implemente uma
# caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser
# informado pelo operador para indicar o final da compra. O programa deve então
# mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra.

while True:
    precosProdutos = []
    precoProduto = True

    while (precoProduto != 0):
        precoProduto = float(input("Digite o preço do produto: "))
        precosProdutos.append(precoProduto)

    print(f"Total: {sum(precosProdutos):,.2f} reais")
    dinheiro = float(input("Insira a quantia que o cliente deu: "))

    while (dinheiro < sum(precosProdutos)):
        dinheiro = float(input("Insira a quantia que o cliente deu: "))

    print(f"Dinheiro: {dinheiro:,.2f} reais")
    print(f"Troco: {(dinheiro - sum(precosProdutos)):,.2f} reais")
