# LISTAS

# Antes
nota1 = 7.5
nota2 = 7.2
nota3 = 7.0

# Com Listas
notas = [7.5, 7.2, 7.0]

# Criando Listas
lista = []
lista = list()
lista = [25, 'Mário Lucas', 3.14, False]
lista = [10, ['a', 'b']]

# Indexação e Slices (fatiamento)
lista = [10, 'Mário', 3.1415, True]
print(lista[0:3])
print(lista[0:])
print(lista[2:6:2])

# Iteração com for para listas
for el in lista:
    print(el)

# Utilizando indices
print(len(lista))

# Percorrendo por indices
for el in range(len(lista)):
    print(lista[el])
