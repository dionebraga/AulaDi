# Solicita ao usuário um número
numero = int(input("olá, caro aluno, digite seu número de matrícula:"))

# Verifica se o número é par ou ímpar e decide o time do aluno
if numero % 2 == 0:
    print(f"você está no time azul.")
else:
    print(f"você está no time amarelo.")