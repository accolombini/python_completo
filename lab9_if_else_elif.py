"""
Estruturas condicionais => if, else e elif >>= chamadas de estruturas condicionais
A diferença aqui é a estrutura elif que quer dizer -> else if -> no Java e em C

"""

idade = 25
if idade < 18:
    print(f'Você ainda não atingiu a maioridade => {idade}')
else:
    print(f'Você já atingiu a maioridade => {idade}')

# Exemplo utilizando elif => que podem ser vários ...:
if idade < 18:
    print(f'Você ainda não atingiu a maioridade => {idade}')
elif idade == 18:
    print(f'Você está com exatos 18 anos => {idade} és adulto!')
elif idade == 25:
    print(f'Você está com 25 anos => {idade} já é Senhor de suas ações!')
else:
    print(f'Você já atingiu a maioridade => {idade}')
