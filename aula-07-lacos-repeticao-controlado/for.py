# ESTRTURA DE REPETIÇÃO CONTROLADA

for var in range(10):
    print(var)

for var in range(1, 10):
    print(var)

for var in range(1, 12, 3):
    print(var)

# CÁLCULO DE MÉDIA AUTOMATIZADA
soma = 0

for i in range(1, 4):
    soma += float(input(f'Informe sua nota {i}: '))

print(f'Sua média foi {soma/3}')
