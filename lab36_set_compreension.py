"""
Set Comprehension ->> lembre-se que set não aceita valores repetidos e não guardam ordenação =>> observe os exemplos

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""

# Exemplo -> gerando um set

numeros = {num for num in range(1, 10)}
print(f'Gerando um Set ->> {numeros}')

# Exemplo -> aplicando conceitos de comprehension in set ->> elevando ao quadrado cada elemento de set

numeros = {quadrado ** 2 for quadrado in numeros}
print(f'Quadrado de um elemento utilizando set -> {numeros}')

# Desafio -> Crie um dicionário a partir dessa estrutura ->> elevando ao quadrado cada elemento de set

numeros = {quadrado: quadrado ** 2 for quadrado in numeros}
print(f'Quadrado de um elemento utilizando set -> {numeros}')

# Exemplo -> trabalhando com strings in sets =>> fique atento em conjunto não há repetição e nem ordenação

letras = {letra for letra in 'Python para Ciência de Dados'}
print(f'Trabalhando com strings in set -> {letras}')
