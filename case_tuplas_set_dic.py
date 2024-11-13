lista =['banana','maça','pera', 'banana']
tuplas = ('casa', 'apartamento', 'casa')
dicionario ={"nome":"Caique", "idade":22,"altura":1.70}
sets = {'gato', 'cachorro', 'pássaro'}

print(lista[0], tuplas[0], dicionario["idade"], list(sets)[0])

#Crie uma tupla com 5 dados
tupla_dados =('pessoa','animal','objeto','planta','animal')

#Altere a tupla para uma lista
lista_dados = list(tupla_dados)

#Asserção:
if isinstance(lista_dados, list) == True:
    print("Esta tupla agora é uma lista")
#Insira 2 dados extras a essa lista
lista_dados.append('surpresa')
print(f"Os elementos contidos na lista são:  {lista_dados}")

'''append(): Adiciona um único elemento ao final.
insert(): Adiciona um elemento em uma posição específica.
extend(): Adiciona múltiplos elementos de uma vez.'''

#Remova o primeiro dado da lista
remover_primeiro_elemento = lista_dados.pop(0)
print(f"Primeiro elemento removido: {remover_primeiro_elemento}")

#Remova o último dado da lista
del lista_dados[-1]
print(f"Último elemento removido: {lista_dados}")
'''pop(0): Remove e retorna o elemento.
del: Remove o elemento sem retornar.'''

#Faça um print com o primeiro dado da lista
print(f"O primeiro elemento da lista é: {lista_dados[0]}")

#Faça um print com a quantidade de dados da lista
quantidade = len(lista_dados)
print(f"A minha lista de dados possui {quantidade} itens.")

'''
Crie um dicionário com os seguintes dados:
Nome, Idade, Profissão
Imprima somente o valor contido na chave Nome do dicionário'''
dic_pessoa ={"Nome":"Caique", "Idade":22, "Profissão": "QA"}
print(f"O valor dentro da chave Nome, é {dic_pessoa['Nome']}")