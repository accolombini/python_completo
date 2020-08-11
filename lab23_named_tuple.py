"""
Módulo Collections -> Named Tuple

Named Tuple -> diz respeito a tupla nomeada => são então tuplas diferenciadas, onde, especificamos
um nome para a mesama e também parâmetros

Para maiores referências: https://docs.python.org/3/library/collections.html
Especificamente vá para: https://docs.python.org/3/library/collections.html#collections.namedtuple

"""

# Para trabalharmos com Tuplas nomeadas precisamos realizar um import


from collections import namedtuple

# Exemplo tupla convencional
tupla = (1, 2, 3)
print(f'Podemos imprimir qualquer elemento da tupla através do seu indice -> {tupla[2]}')

# Exemplo de tupla nomeadas. Após o import precisamos definir nomes e parâmetros
# Forma 1 -> Declaração => NamedTuple <-> observe que estamos separando por espaços
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 -> Declaração => NamedTuple <-> observe que estamos separando por vírgulas
cachorro2 = namedtuple('cachorro2', 'idade, raca, nome')

# Forma 3 -> Declaração => NamedTuple <-> observe que estamos trabalhando com uma lista para os parâmetros
cachorro3 = namedtuple('cachorro3', ['idade', 'raca', 'nome'])

# Utilizando as declrações feitas nas três formas acima -> Forma 1
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(f'Implimindo NamedTupla Forma 1 -> {ray} - seu tipo é -> {type(ray)}')
# Acessando os dados forma 1
print(f'Acessando elemento da NamedTupla com os indices exemplo indice [0] (idade) -> {ray[0]}')
print(f'Acessando elemento da NamedTupla com os indices exemplo indice [1] (raça) -> {ray[1]}')
print(f'Acessando elemento da NamedTupla com os indices exemplo indice [2] (nome) -> {ray[2]}')
print(f'-----------------------------Espaço-----------------------------')

# Acessando os dados forma 2
print(f'Acessando elemento da NamedTupla com operador ponto (idade) -> {ray.idade}')
print(f'Acessando elemento da NamedTupla com operador ponto (raça) -> {ray.raca}')
print(f'Acessando elemento da NamedTupla com operador ponto (nome) -> {ray.nome}')
print(f'-----------------------------Espaço-----------------------------')

# Tudo o já aprendido em Tuplas se aplicam aqui, veja alguns exemplos

print(f'Qual o indice da idade? -> {ray.index(2)}')
print(f'Qual o índice da raça? -> {ray.index("Chow-Chow")}')
print(f'Qual o indice do nome? -> {ray.index("Ray")}')
print(f'Quantos Chow-Chow temos? -> {ray.count("Chow-Chow")}')

print(f'-----------------------------Espaço-----------------------------')

# Utilizando as declrações feitas nas três formas acima -> Forma 2
ray = cachorro2(idade=2, raca='Chow-Chow', nome='Ray')
print(f'Implimindo NamedTupla Forma 2 -> {ray} - seu tipo é -> {type(ray)}')
print(f'-----------------------------Espaço-----------------------------')

# Utilizando as declrações feitas nas três formas acima -> Forma 3
ray = cachorro3(idade=2, raca='Chow-Chow', nome='Ray')
print(f'Implimindo NamedTupla Forma 3 -> {ray} - seu tipo é -> {type(ray)}')
