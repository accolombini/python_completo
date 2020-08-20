"""
Sorted =>> eleva o poder da função sort() que só pode ser utilizada com listas

    - Sorted =>> a função sorted() pode ser usado com qualquer iterável.
    - Como o próprio nome sugere =>> sorted() tem por função ordenar.
    - Independente do iterável =>> sorted() sempre retornará uma lista mantendo intacto o iterável original

"""
# Relembrando sort() em listas

l1 = [4, 33, 5, 1, 0, 199, 2, 200]
l1.sort()  # sort() não tem retorno ou seu retorno é None ->> Fique atento

print(f'Relembrando sort() -> {l1}')

# Relembrando sort() observe o que acontece quando se tenta usar sort() com uma tupla

# T1 = (4, 33, 5, 1, 0, 199, 2, 200)
# T1.sort()  # AttributeError: 'tuple' object has no attribute 'sort'

# print(f'Relembrando sort() -> {T1}')

# Exemplo de uso do sorted() ->> fique atento ao retorno da lista

numeros = [6, 1, 8, 2]
print(f'Nossa lita de teste para sorted() -> {numeros}')
print(f'Ordenando com sorted() -> {sorted(numeros)}')  # Observe a primeira diferença -> sorte() retorna valor
# O uso de sorted() retorna uma nova lista classificada deixando a lista original intacta ->> observe
print(f'Nossa lita de teste após o uso de sorted() -> {numeros}')
numeros = (6, 1, 8, 2)
print(f'Nossa tupla de teste para sorted() -> {numeros}')
print(f'Ordenando a tupla com sorted() retorno serfá uma lista -> {sorted(numeros)}')
numeros = {6, 1, 8, 2}
print(f'Nosso conjunto de teste para sorted() -> {numeros}')
print(f'Ordenando com sorted() retorno será uma lista -> {sorted(numeros)}')
numeros = {7: 6, 20: 1, 333: 8, 1: 2}
print(f'Nosso dicionário de teste para sorted() -> {numeros}')
print(f'Ordenando com sorted() retorno será uma lista -> {sorted(numeros)}')  # Ordena as chaves por default

print(f'\n-------------------------sorted()---------------------------\n')
# Adicionando parâmetros ao sorted() e empoderando sua capacidade de classificação
numeros = {6, 1, 8, 2}
print(f'Nosso conjunto de teste para sorted() -> {numeros}')
# O retorno será uma lista ordenada e na forma reversa
print(f'Ordenando com sorted() com parâmetro reverse -> {sorted(numeros, reverse=True)}')

# Podemos usar o sorted() para assões maos complexas

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cahorro', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

print(f'Conhecendo os dados -> {usuarios}')
# print(f'Classificando com sorted -> dicionário {sorted(usuarios)}')  # TypeError: '<' not supported between instances of 'dict' and 'dict'
# Observe pelo erro que ele não consegue ordenar uma lista contendo um dicionário, neste caso você deve ...
# Com key=len implica ordenação por tamanho
print(f'Classificando nossa lista com dicionário -> usando key {sorted(usuarios, key=len)}')

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], "cor": 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cahorro', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], "cor": "preto", "musica": "rock"},
]

# Com key=com lamda nestecaso ordenaremos pelo username
print(
    f'Classificando nossa lista com dicionário -> usando key {sorted(usuarios, key=lambda usuario: usuario["username"])}')

# Vamos agora ordenar em ordem reversa
print(
    f'Classificando em ordem reversa nossa lista com dicionário -> usando key {sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True)}')

# Vamos agora ordenar pelo número de Tweets do menor para o maior
print(
    f'Classificando por número de tweets nossa lista com dicionário -> usando key {sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))}')

# Para encerrar ->> fique atento ao grau de complexidade Python avançado

musicas = [
    {"titulo": "Thundestruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32}
]

# Desafio será classificar pelas mais tocadas
print(f'Classificando musicas pelas mais tocadas -> {sorted(musicas, key=lambda musica: musica["tocou"], reverse=True)}')
