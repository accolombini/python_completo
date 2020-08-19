"""
Dictionary Comprehension ->> Se quisermos criar um dicionário fazemos => dicionario={'a': 1, 'b': 2, 'c': 3, 'd': 4}

Se quisermos criar uma lista fazemos => lista=[1, 2, 3, 4]
Se quisermos criar uma tupla fazemos => tupla=(1, 2, 3, 4) ou tupla = 1, 2, 3, 4
Se quisermos criar um set (conjunto) fazemos => conjunto={1, 2, 3, 4}

    - Sintaxe Dictionary Comprehension =>> {chave:valor(operação) for valor in iterável}
    - Iterável aqui é um discionário ->> para trabalhar com os outros iteráveis terá que utilizar chave/valor como
    se fosse uma única variável divergindo na operação, portanto, fique atento, não existe dicionários com chaves
    repetidas ->> confira no exemplo

"""
# Exemplos -> comprehension usando dicionários

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Queremos elevar ao quadrado os valores de dict
quadrado = {letra: valor ** 2 for letra, valor in numeros.items()}
print(f'Usando Comphehension in dict -> {quadrado}')

# Exemplos -> comprehension dicionários a partir de uma lista =>> observe como estamos trabalhando com chave/valor

numeros = [1, 2, 3, 4, 5]
cubo = {valor: valor ** 3 for valor in numeros}
print(f'Usando Comphehension in dict a partir de lista -> {cubo}')

# Exemplos -> comprehension dicionários a partir de uma tupla =>> observe como estamos trabalhando com chave/valor

numeros = (1, 2, 3, 4, 5)
cubo = {valor: valor ** 3 for valor in numeros}
print(f'Usando Comphehension in dict a partir de tupla -> {cubo}')

# Exemplos -> comprehension dicionários a partir de um conjunto =>> observe como estamos trabalhando com chave/valor

numeros = {1, 2, 3, 4, 5}
cubo = {valor: valor ** 3 for valor in numeros}
print(f'Usando Comphehension in dict a partir de conjunto -> {cubo}')

# Exemplos -> comprehension dicionários a partir de uma lista tendo valores repetidos =>> observe como estamos trabalhando com chave/valor e mais ainda, verifique o que acontece com os valores repetidos

numeros = [1, 2, 3, 4, 5, 4, 3, 2, 1]  # Note a presença de valores repetidos
cubo = {valor: valor ** 3 for valor in numeros}
print(f'Usando Comphehension in dict a partir da lista -> {numeros}\nA partir de uma lista com valores repetidos -> {cubo}\nObserve o resultado das chaves')

# Exemplo -> complicando um pouco -> Veja como usar Dict Comprehension para gerar um dicionário a partir
# de uma string utilizada como chave e uma lista utilizada como valores

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(f'O Resultado dessa mistruar é -> {mistura}')

# Exemplo utilizando lógica condicional ->> neste dicionário a chave será o próprio valor da lista
# os valores serão par -> quando o número for par e ímpar -> quando o número for ímpar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = {num: ('par' if not num % 2 else 'impar') for num in numeros}
print(f'O valor de dict comprehension com lógica condicional é -> {res}')
