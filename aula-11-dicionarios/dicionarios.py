# DICIONÁRIOS

# Criando dicionários
dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Mário Lucas',
    'idade': 26,
    'altura': 1.69
}

print(dicionario)
print(dicionario['nome'])

# Adicionando valores em dicionário
dicionario['programador'] = True
print(dicionario)

for chave in dicionario:
    print(dicionario[chave])

# Testar se chave já existe
print('peso' in dicionario)
print('idade' in dicionario)
