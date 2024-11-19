# Definindo dois dicionários
dicionario1 = {"nome": "Dione", "idade": 40}
dicionario2 = {"nome": "Diony", "idade": 39}

# Criando uma lista com nome e idade de ambos os dicionários
dados = [
    f"{dicionario1['nome']} ({dicionario1['idade']} anos)",
    f"{dicionario2['nome']} ({dicionario2['idade']} anos)"
]

# Imprimindo os dados em uma única linha
print(f"Os dados coletados são: {', '.join(dados)}")