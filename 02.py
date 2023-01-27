# Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

nome = input("Insira seu nome: ")
senha = input("Insira sua senha: ")

while (nome == senha):
    senha = int(input("Insira uma senha válida: "))
    if (nome != senha):
        print("Seja bem-vindo!")
        exit()


print("Seja bem-vindo!")
