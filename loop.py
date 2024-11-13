lista =['banana','maça','pera', 'banana']
for frutas in lista:
    print (f"Os elementos contidos na lista são: {frutas}")

dicionario = {"nome": "Caique", "idade": 22}

for chave in dicionario:
    print (f"As chaves neste dicionário são: {chave}")

for valor in dicionario.values():
    print (f"Os valores neste dicionário são: {valor}")

    '''Listas: Ao iterar sobre uma lista, você acessa cada item da lista em ordem.
    Strings: Ao iterar sobre uma string, você acessa cada caractere.
    Tuplas: Quando você itera sobre uma tupla, acessa cada elemento na ordem em que foram definidos.
    Conjuntos (Sets): Ao iterar, você acessa os elementos, mas a ordem não é garantida, já que conjuntos não mantêm a sequência.
    
    '''