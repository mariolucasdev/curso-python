# FUNÇÕES

# Criação de funções
def saudacao(nome, curso):
    print(f'Seja bem vindo(a) {nome}!')
    print(f'É um prazer te você fazendo o curso de {curso}!')


saudacao('Mário Lucas', 'Python')

# Funções parâmetro default


def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo(a) {nome}!')
    print(f'É um prazer te você fazendo o curso de {curso}!')


saudacao('Mario Lucas')

# Funções com retorno


def soma(num1, num2):
    return num1 + num2


resultado = soma(1, 2)
print(f'O resultado da soma é igual á: {resultado}')
