# LAÇOS DE REPETIÇÃO

from random import randint

numero_sorteado = randint(1, 10)
numero_escolhido = int(input('Informe um número entre 1 e 10: '))

while numero_escolhido != numero_sorteado:
    print('Você errou, tente novamente')
    numero_escolhido = int(input('Informe um número entre 1 e 10: '))

print('Parabéns você acertou!')

# EXEMPLO 2 ESTRUTURA COM CONTADOR

contador = 0

while contador < 5:
    contador = contador + 1
    print(contador)
