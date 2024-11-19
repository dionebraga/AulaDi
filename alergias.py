# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Lista de alergias (você pode adicionar manualmente as frutas alérgicas aqui)
alergias = ["amendoim", "morango"]

# Adicionando uma fruta da lista de frutas à lista de alergias
alergias.append("banana")  # Exemplo de adicionar uma fruta que já está na lista de frutas

# Estrutura para verificar se cada fruta está na lista de alergias
print("Frutas na lista de alergias:")
for fruta in frutas:
    if fruta in alergias:  # Verifica se a fruta está na lista de alergias
        print(fruta)  # Imprime o nome da fruta que está na lista de alergias
