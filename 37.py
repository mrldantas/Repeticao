# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa
# que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
# no campo código. Ao encerrar o programa também deve ser informados os códigos e
# valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além
# da média das alturas e dos pesos dos clientes

codigoClientes = []
alturaClientes = []
pesoClientes = []

codigo = True

while (codigo != 0):
    codigo = int(input("Insira o código: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Insira a altura: "))
        peso = float(input("Insira o peso: "))
        codigoClientes.append(codigo)
        alturaClientes.append(altura)
        pesoClientes.append(peso)

codigoMagro = pesoClientes.index(min(pesoClientes))
codigoGordo = pesoClientes.index(max(pesoClientes))
codigoBaixo = alturaClientes.index(min(alturaClientes))
codigoAlto = alturaClientes.index(max(alturaClientes))

print(f"Mais magro: {codigoClientes[codigoMagro]}")
print(f"Mais gordo: {codigoClientes[codigoGordo]}")
print(f"Mais baixo: {codigoClientes[codigoBaixo]}")
print(f"Mais alto: {codigoClientes[codigoAlto]}")
print(f"Média de altura: {round(sum(alturaClientes) / len(alturaClientes))}cm")
print(f"Média de peso: {sum(pesoClientes) / len(pesoClientes)}kg")
