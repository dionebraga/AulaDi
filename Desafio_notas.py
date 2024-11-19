'''Desafio: Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.'''

nota1 = int(input("Insira a nota do semestre 01: "))
nota2 = int(input("Insira a nota do semestre 02: "))
nota3 = int(input("Insira a nota do semestre 03: "))
nota4 = int(input("Insira a nota do semestre 04: "))

soma = nota1 + nota2 + nota3 + nota4

media = soma/4

print(f"“Olá, Caique! Sua média é: {media} pontos”")