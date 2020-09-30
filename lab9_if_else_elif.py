"""
Estruturas condicionais => if, else e elif >>= chamadas de estruturas condicionais
A diferença aqui é a estrutura elif que quer dizer -> else if -> no Java e em C

"""

idade = 25
if idade < 18:
    print(f'Você ainda não atingiu a maioridade => {idade} anos')
else:
    print(f'Você já atingiu a maioridade => {idade} anos')

# Exemplo utilizando elif => que podem ser vários ...:
if idade < 18:
    print(f'Você ainda não atingiu a maioridade => {idade} anos')
elif idade == 18:
    print(f'Você está com exatos => {idade} anos és adulto!')
elif idade == 25:
    print(f'Você está com => {idade} anos e já é Senhor de suas ações!')
else:
    print(f'Você já atingiu a maioridade você está com => {idade} anos')
