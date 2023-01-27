# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


codigos = [100, 101, 102, 103, 104, 105]
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True

pedido = []

print(
    "|  Especificação  | Código |   Preço   |"
    "\n----------------------------------------"
    "\n| Cachorro Quente |  100   |  R$ 1,20  |"
    "\n| Bauru Simples   |  101   |  R$ 1,30  |"
    "\n| Bauru com ovo   |  102   |  R$ 1,50  |"
    "\n| Hámburguer      |  103   |  R$ 1,20  |"
    "\n| Cheeseburguer   |  104   |  R$ 1,30  |"
    "\n| Refrigerante    |  105   |  R$ 1,00  |"
)

while (codigo != 0):
    codigo = int(input("\nInsira o código do produto: "))
    if (codigo == 0):
        break
    else:
        while codigo not in codigos:
            codigo = int(input("Insira um código válido: "))
        numero = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valorPedido = precos[numero] * quantidade
        pedido.append(valorPedido)

print(f"Total: {round(sum(pedido))} reais")
