# CONVERSÃO DE TIPOS

from unicodedata import numeric

idade  = '26'

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# int()
# str()
# float()
# bool()

altura = float(input('Informa sua altura:'))

print(altura, type(altura))