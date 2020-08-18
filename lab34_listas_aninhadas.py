"""
Listas Aninhadas (Nested Lists) ->> em Python não existem arrays =>> Python possui Listas

    - Algumas linguagends de programação possuem uma estrutura de dados chamadas de arrays:
        - Unidimensionais ->> (Arrays/Vetores)
        - Multidimensionais ->> (matrizes)

"""

# Exemplos -> veja uma Matriz 3 x 3 a partir de listas aninhadas

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Trabalhando com listas aninhadas -> {listas}\nSeu tipo é -> {type(listas)}')

# Como podemos acessar dados em listas aninhadas -> observe a construção do exemplo, isso vale para
# listas com maior grau de complexidade =>> Lembrando que podemos utilizar índices negativos nas listas

print(f'Primeiro elemento da primeira linha -> {listas[0][0]}')
print(f'Segundo elemento da primeira linha -> {listas[0][1]}')
print(f'Terceiro elemento da primeira linha -> {listas[0][2]}')
print(f'Primeiro elemento da segunda linha -> {listas[1][0]}')
print(f'Segundo elemento da segunda linha -> {listas[1][1]}')
print(f'Terceiro elemento da segunda linha -> {listas[1][2]}')
print(f'Primeiro elemento da terceira linha -> {listas[2][0]}')
print(f'Segundo elemento da terceira linha -> {listas[2][1]}')
print(f'Terceiro elemento da terceira linha -> {listas[2][2]}')

# Iterando com loop em listas aninhadas

for lista in listas:
    for num in lista:
        print(f'Iteirando em lista aninhadas -> {num}')

# Usando list comphehension para imprimir todos -> observe a tupla com os índices das linhas
print(f'Usando list Comprehension -> {[numero for numero in enumerate(listas)]}')
print(f'Usando list Comprehension refatorado -> observe o uso da função print()')
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos -> gerando um tabuleiro #x3

print(f'Numa linha -> {[[numero for numero in range(1, 4)] for valor in range(1, 4)]}')

# Em mais de uma linha
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(f'Em mais de uma linha -> {tabuleiro}')

# Gerando resultados utilizando condicional -> escreve X se for par e 0 se for ímpar

resultado = [['X' if not numero % 2 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(f'O resultado do jogo da velha é -> {resultado}')

# Gerando valores iniciais => inicilizando uma lista aninhada com List Comprehension "matriz 4x5"

print(f'Inicializando uma lista -> {[["*" for i in range(1, 6)] for j in range(1, 5)]}')
