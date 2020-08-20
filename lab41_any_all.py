"""
Any e All ->> fazem parte da biblioteca padrão do Python

    - all() =>> retorna True se todos os elementos do iterável forem verdadeiros ou ainda se o iterável estiver vazio
    - any() =>> retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False

"""

# Exemplo ->> uso de all()
# Neste exemplo observe a presença do número 0 na lista, o que para Python é False
print(f'Observe o retorno de all() neste exemplo -> {all([0, 1, 2, 3, 4, 5])}')
# Neste exemplo observe que tiramos o número 0 na lista
print(f'Observe o retorno de all() neste exemplo -> {all([1, 2, 3, 4, 5])}')
# Neste exemplo observe que a lista está vazia o que para all() é True
print(f'Observe o retorno de all() neste exemplo -> {all([])}')
# Lembre-se que podemos trabalhar com qualquer iterável Python
print(f'Observe o retorno de all() neste exemplo set -> {all({1, 2, 3, 4, 5})}')
print(f'Observe o retorno de all() neste exemplo tupla -> {all((1, 2, 3, 4, 5))}')
print(f'Observe o retorno de all() neste exemplo string -> {all("Python para Ciência de Dados")}')

# Podemos utilizar esse recurso dentro de um for ->> acompanhe =>> note que todos os nomes iniciam com a letra "C"

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

# Observe o uso de list comprehension =>> como todos os nomes inicial em "C" o retorno será True

print(f'Python avançado com all() -> {all([nome[0] == "C" for nome in nomes])}')

nomes = ['Carlos', 'Pedro', 'Carla', 'Cassiano', 'Julia']

# Observe o uso de list comprehension =>> como nem todos os nomes inicial em "C" o retorno será False

print(f'Python avançado com all() -> {all([nome[0] == "C" for nome in nomes])}')

# É uma boa alternativa para se fazer alguma verificação, veja neste exemplo a seguir =>> você poderá criar o que quiser

print(f'Checando com all() -> {all([letra for letra in "eio" if letra in "ximano"])}')

# FIQUE ATENTO, se você esperava no exemplo acima receber False, lembre-se que para all() uma lista vazia []
# ou seja sem qualquer coincidência com o que você está buscando, é por all() considerado True

# No exemplo a seguir vamos testar se todos os números de uma lista são pares

print(f'São todos pares? com all() -> {all([num for num in [2, 4, 6, 8, 10, 10000] if not num % 2])}')

print(f'------------------------------------any()----------------------------------------')
# Exemplo ->> uso de any()

print(f'Observe o retorno de any() neste exemplo -> {any([0, 1, 2, 3, 4, 5])}')
# Neste exemplo observe que a lista está vazia o que para any() é False
print(f'Observe o retorno de any() neste exemplo -> {any([])}')
# Lembre-se que podemos trabalhar com qualquer iterável Python
print(f'Observe o retorno de any() neste exemplo set -> {any({1, 2, 3, 4, 5})}')
print(f'Observe o retorno de any() neste exemplo tupla -> {any((1, 2, 3, 4, 5))}')
print(f'Observe o retorno de any() neste exemplo string -> {any("Python para Ciência de Dados")}')
print(f'Observe o retorno de any() quandos todos forem falsos -> {any([0, False, {}, (), []])}')
print(f'Observe o retorno de any() um verdadeiro -> {any([0, False, {}, (), [], "Show"])}')
nomes = ['Carlos', 'Pedro', 'Carla', 'Cassiano', 'Julia']

# Observe o uso de list comprehension =>> como nem todos os nomes inicial em "C" o retorno será False

print(f'Python avançado com any() -> {any([nome[0] == "C" for nome in nomes])}')

# No exemplo a seguir vamos testar se todos os números de uma lista são pares ->> observe com any() trabalha
# se ao menos um dos resultados forem verdadeiros ele retorna True =>> FIQUE ATENTO

print(f'São todos pares? com any() -> {any([num for num in [2, 4, 6, 8, 10, 10000] if not num % 2])}')
print(f'São todos pares? com any() -> {any([num for num in [2, 4, 6, 8, 10, 23, 10000] if not num % 2])}')
print(f'São todos pares? com any() -> {any([num for num in [3, 5, 7, 89, 11, 23, 10000] if not num % 2])}')
print(f'São todos pares? com any() -> {any([num for num in [3, 5, 7, 89, 11, 23, 10001] if not num % 2])}')
