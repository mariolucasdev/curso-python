# METODOS E FUNÇÕES DE LISTAS

lista = [1, 3, 12, 8, 2]

# append

print('Antendos do append: ', lista)
lista.append(3)
print('Depois do append: ', lista)

# insert

print('Antendos do insert: ', lista)
lista.insert(2, 10)
print('Depois do insert: ', lista)

# extend
lista2 = [1, 2, 3]

print('Antendos do extend: ', lista)
lista.extend(lista2)
print('Depois do extend: ', lista)

# pop
lista.pop()
print(lista)

lista.pop(0)
print(lista)

# remove
lista.remove(3)
print('Depois do remove: ', lista)

# count
# número de ocorrência na lista
lista.count(2)

# index
lista.index(12)

# sort
lista.sort()
lista.sort(reverse=True)

# len
len(lista)

# sum
sum(lista)

# max
max(lista)

# min
min(lista)