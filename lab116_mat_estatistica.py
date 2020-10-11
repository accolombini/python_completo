"""
Novidades da versão 3.8 => matemática e estatística

            - math.prod => retorna o produto de um container numérico
"""

import math
import statistics

# Trabalhando com math.prod

nums_v1 = [2, 3, 6, 8]
nums_v2 = 2, 3, 6, 8
nums_v3 = {2, 3, 6, 8}

print(f'Trabalhando com math.prod em listas -> {math.prod(nums_v1)}')
print(f'Trabalhando com math.prod em tuplas -> {math.prod(nums_v2)}')
print(f'Trabalhando com math.prod em conjuntos -> {math.prod(nums_v3)}')

# Trabalhando com math.isqrt => devolve a parte inteira de uma reaiz ->> ATENÇÃO ele não arredonda valores

print(f'Trabalhando com math.isqrt -> {math.isqrt(9):.2f}')
print(f'Trabalhando com math.sqrt -> {math.sqrt(9):.2f}')
print(f'Trabalhando com math.isqrt -> {math.isqrt(17):.2f}')
print(f'Trabalhando com math.sqrt -> {math.sqrt(17):.2f}')
print(f'Trabalhando com math.isqrt -> {math.isqrt(33):.2f}')
print(f'Trabalhando com math.sqrt -> {math.sqrt(33):.2f}')

# Trabalhando com math.dist => retorna a distância euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D

p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D

p2d1 = [12, 50]
p2d2 = [6, 7]

print(f'Teste distância Euclidiana 3D -> {math.dist(p3d1, p3d2):.5f}')
print(f'Teste distância Euclidiana 2D -> {math.dist(p2d1, p2d2):.5f}')

# Trabalhando com math.hypot => retorna a hipotenusa ou a norma Euclidiana
# Atenção -> observe o uso do * ele é necessário para descompactar a lista/tupla/ etc e retornar os valores

print(f'Ilustrando o retorno do * -> ', *p3d1)  # Ilustrando o retorno do * ->  12 50 40
print(f'Teste norma Euclidiana 3D -> {math.hypot(*p3d1):.5f}')
print(f'Teste norma Euclidiana 2D -> {math.hypot(*p2d1):.5f}')

# Em estatística nós temos:

# statistics.fmean -> calcula a média de números reais => todos os valores serão convertidos em reais
# O resultado de statistics.fmean() sempre será real

valores_reais = [1.45, 6.789, 3.45, 89.89765]
valores_inteiros = [1, 6, 3, 89]

print(f'Teste de statistics.fmean Reais -> {statistics.fmean(valores_reais)}')  # 25.396662499999998
print(f'Teste de statistics.fmean Inteiros -> {statistics.fmean(valores_inteiros)}')  # 24.75

# statistics.geometric_mean => calcula a média geométrica de números reais

print(f'Teste de statistics.geometric_mean() Reais -> {statistics.geometric_mean(valores_reais)}')  # 7.433362480574992
print(f'Teste de statistics.geometric_mean() Inteiros -> {statistics.geometric_mean(valores_inteiros)}')
# 6.326530818100785

# statistics.multimode => retorna o valor mais frequente em uma sequencia

seq1 = 'Python para Ciencia de Dados'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(f'Testando statistics.multimode -> {statistics.multimode(seq1)}')  # [' ', 'a']
print(f'Testando statistics.multimode -> {statistics.multimode(seq2)}')  # [3]
print(f'Testando statistics.multimode -> {statistics.multimode(seq3)}')  # [1, 2, 3]
