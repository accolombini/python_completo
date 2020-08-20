"""
Generator Expression =>> também conhecidas como Tuple Comprehension

    ATENÇÃO:    o generator retorna um <class 'generator'> que assim como os Comprehension ao ser convertido com um                  cast será zerado ->> muito importante =>> Fique atento
                Quando o assunto for porformance =>> para o mesmo projeto ->> Generators possuem uma melhor resposta a               performance que o List Comprehension, Set Comprehension e Dictionary Comprehension


    - O que sabemos:
        - List Comprehension
        - Dictionary Comprehension
        - Set Comprehension

"""
# Para avaliarmos a performnce precisaremos fazer um import

from sys import getsizeof

# Recapitulando o último laboratório - Lab41
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f'Python avançado com any() -> {any([nome[0] == "C" for nome in nomes])}')

# Podemos fazer o mesmo de forma mais efetiva utilizando Generators
print(f'Python avançado com Generators e any() -> {any(nome[0] == "C" for nome in nomes)}')
ret = (nome[0] == "C" for nome in nomes)
print(f'O retorno de um Generator é do tipo -> {type(ret)}')  # <class 'generator'>
ret = [nome[0] == "C" for nome in nomes]
print(f'O retorno de um list comprehension é do tipo -> {type(ret)}')  # <class 'list'>
# Note que no exemplo anterior utilizamos list Comprehension e neste usamos Generators ->> tuplas

print(f'\n------------------------------Performance----------------------------------')
# A função de getsizeof() é retornar a quantidade de bytes em memória do elemento passado como argumento
# O resultado será o número de bytes em memória que o argumento está ocupando

print(f'Testando a função getsizeof() teste string longo -> {getsizeof("Python para Ciência de Dadors")}')
print(f'Testando a função getsizeof() teste string curto -> {getsizeof("Python")}')
print(f'Testando a função getsizeof() teste numero curto -> {getsizeof(5)}')
print(f'Testando a função getsizeof() teste numero longo -> {getsizeof(5678899764321)}')
print(f'Testando a função getsizeof() teste Bolean -> {getsizeof(True)}')

# Gerando uma lista numércia com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista numércia com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista numércia com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista numércia com Generators
generators = getsizeof((x * 10 for x in range(1000)))

print(f'Comparando performance ->> List ... {list_comp} - bytes')  # 9016
print(f'Comparando performance ->> Set ... {set_comp} - bytes')    # 32984
print(f'Comparando performance ->> Dict ... {dict_comp} - bytes')  # 36960
print(f'Comparando performance ->> Generators ... {generators} - bytes')  # 112

# Vamos agora iteirar no Generators Expression
gen = (x * 10 for x in range(1000))
print(f'Confirmando o tipo do generator -> {type(gen)}')   # <class 'generator'>
for num in gen:
    print(f'Iteirando com generators {num}')

print(f'Imprimindo o conteúdo de um generator -> {tuple(gen)}')  # () isto ocorre porque já usamos o conteúdo de gen

gen = (x * 10 for x in range(1000))
print(f'Imprimindo o conteúdo de um generator -> {tuple(gen)}')  # Tudo ok, pois geramos novamente um Generator
