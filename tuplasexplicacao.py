# Definindo a lista, tupla, set e dicionário
lista = ['banana', 'maçã', 'pera']  # Corrigido o erro de digitação em "maçã"
tupla = (1, 2, 3, 4, 5)
meu_set = {1, 2, 3, 4}
dicionario = {"nome": "Caique", "idade": 22}

# Função para adicionar frutas à lista
def add_fruta(a, b):
    lista.append(a)  # Adiciona a fruta "a"
    lista.append(b)  # Adiciona a fruta "b"
    print(lista)     # Imprime a lista após adicionar as frutas

# Chamada da função add_fruta
add_fruta("Limão", "Morango")  # Adiciona "Limão" e "Morango" à lista

# Função para remover a primeira fruta da lista
def del_fruta():
    lista.pop(0)  # Remove o primeiro item da lista
    print(lista)  # Imprime a lista após remover o primeiro item

# Exibindo os elementos da lista
for frutas in lista:
    print(f"Os elementos contidos na lista são: {frutas}")  # Exibe cada fruta da lista

# Iterando sobre uma string e exibindo cada letra
var_txt = "Texto"
for letras in var_txt:
    print(letras)  # Exibe cada letra da string "Texto"

# Iterando sobre a lista novamente
for x in lista:
    print(f"Os elementos da lista são {x}")  # Exibe cada elemento da lista

# Dicionário com chave "Nome" e "idade"
dicionario = {"Nome": "Caique", "idade": 22}

# Iterando sobre o dicionário para imprimir as chaves e valores
for chave, valor in dicionario.items():  # Corrigido o método para items()
    print(f"Chave: {chave}, Valor: {valor}")  # Exibe chave e valor do dicionário
