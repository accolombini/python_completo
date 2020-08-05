"""
Mapas => são conhecidos em Python como Didicionários
Dicionários em Python são representados por chaves {}

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400, 'abr': 600}

print(f'O dicionário de testes é -> {receita} - e seu tipo é {type(receita)}')

# Como inteirar sobre dicionários
for chave in receita:
    print(f'Em receita temos as chaves -> {chave} - e os valores {receita[chave]}')
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Podemos facilmente conhecer todas as chaves de um dicionário com o método .keys()
print(f'As chaves presentes no dicionári {receita} - são -> {receita.keys()} - seu tipo é => {type(receita.keys())}')

# Outro exemplo de interação utilizando o dicionário de chaves => forma Pythonica para iteração
for chave in receita.keys():
    print(f'Usando o dicionário .keys() chave => {chave} - valor => {receita[chave]}')

# Acessando os valores de um dicionário -> o método .values() retorno um dicionário de valores
print(f'Acessando os valores de um dicionário -> {receita.values()} - e seu tipo é {type(receita.values())}')
print(f'Acessando as chaves e os valores de um dicionário -> {receita.keys()} : {receita.values()}')

for valor in receita.values():  # => forma Pythonica para iteração -> valores
    print(f'Valores do dicionário receita => {valor}')

# Desempacotamento de dicionáros -> uso doo método items()
print(f'Conhecendo items() -> {receita.items()} - e seu tipo é -> {type(receita.items())}')
for chave, valor in receita.items():
    print(f'Desempacotando o dicionário: chave = {chave} e valor = {valor}')

# Soma*, Valor Máximo*, Valor mínimo*, Tamanho => válidos para valores numéricos
print(f'A soma de receita é => {sum(receita.values())}')
print(f'O valor máximo de receita é => {max(receita.values())}')
print(f'O valor mínimo de receita é => {min(receita.values())}')
print(f'A dimensão do dicionário receita é => {len(receita)}')
