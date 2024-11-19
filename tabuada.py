# Solicita ao usuário um número para gerar a tabuada
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")

# Estrutura de repetição para calcular e exibir a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
