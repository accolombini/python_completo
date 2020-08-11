"""
Módulo Collections => Ordered Dict -> é um dicionário como já aprendido, com a diferença de que ele
irá garantir a ordem do dicionário sempre (ordem de inserção)

NOTA: Lembre-se que tudo que utilizar dentro do Collections terá uma performance maior

Para maiores informações: https://docs.python.org/3/library/collections.html
Especificamente vá para: https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""

# Em um dicionário, a ordem de inserção dos elementos não é garantida -> consulte na fonte com: help({})


# Para trabalhar com Orderd Dict precisamos fazer um import
from collections import OrderedDict


# Exemplo dicionário padrão
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f'Imprimindo o dicionário -> {dicionario} - seu tipo é -> {type(dicionario)}')

for chave, valor in dicionario.items():
    print(f'Cahve = {chave}: valor = {valor}')

print(f'-------------------- Espaço ----------------------')
# Exemplo Ordered Dict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'No OrderedDict => Cahve = {chave}: valor = {valor}')

print(f'-------------------- Espaço ----------------------')

# Entendendo a diferença entre Dict e Orederd Dict
# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(f'Imprimindo dict1 -> {dict1} \nImprimindo dict2 -> {dict2}')
print(f'Avaliando se dict1 é igual a dict2 -> {dict1 == dict2}')
# Note que o retorno será True, já que a ordem dos elementos não importam para o dicionário

print(f'-------------------- Espaço ----------------------')

# Entendendo a diferença entre Dict e Orederd Dict
# Dicionários Ordered Dict
dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})
print(f'Imprimindo dict1 -> {dict1} \nImprimindo dict2 -> {dict2}')
print(f'Avaliando se dict1 é igual a dict2 -> {dict1 == dict2}')
# Note que o retorno será False, já que a ordem dos elementos é importante para o dicionário
