# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira o nome: ")
while (len(nome) <= 3):
    nome = input("Insira o nome: ")

idade = int(input("Insira sua idade: "))
while (0 > idade) or (idade > 150):
    idade = int(input("Insira sua idade: "))

salario = float(input("Insira seu salário: "))
while (salario < 0):
    salario = float(input("Insira seu salário: "))

sexo = input("Insira F para feminino e M para masculino: ")
while (sexo != "F") and (sexo != "M"):
    sexo = input("Insira F para feminino e M para masculino: ")

estado = input("Insira seu estado civil [S, C, V ou D]: ")
while (estado != "S") and (estado != "C") and (estado != "V") and (estado != "D"):
    estado = input("Insira seu estado civil [S, C, V ou D]: ")
