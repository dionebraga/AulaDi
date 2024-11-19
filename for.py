# Imprimindo todos os números de 1 até 1000
print("Todos os números de 1 a 1000:")
for num in range(1, 1001):
    print(num)

# Imprimindo apenas os números pares de 1 até 1000
print("\nNúmeros pares de 1 a 1000:")
for num in range(1, 1001):
    if num % 2 == 0:  # Verifica se o número é divisível por 2
        print(num)
