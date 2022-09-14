# ESTRUTURAS CONDICIONAIS

idade = 17

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade')

# VERIFICANDO APROVAÇÃO

media = float(input('Informe a média do estudande:'))

if media >= 7:
    print('Você foi aprovado(a)!')
elif media >= 5:
    print('Recuperaçao!')
else:
    print('Você foi reprovado(a)!')

# APROVAÇÃO COM FALTAS

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovada(o)')
else:
    print('Reprovada(o)')
