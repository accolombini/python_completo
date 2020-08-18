"""
List Comprehension ->> utilizando List Comprehension nós podemos gerar novas listas com dados processados
a partir de outro iterável (uma coleção de dados)

    - Sintaxe da List Comprehension
    - [dado clausula for dado in itervael]

    <$> Para melhor entender o que está acontecendo devemos dividir a expressão em duas partes:
        - A primeira parte: for dado in iteravel
        - A segunda parte: dado <-> aplica-se a operação expressa em clausula

"""

# Exemplos

numeros = [1, 2, 3, 4, 5]  # Nosso iterável exemplo
print(f'Neste primeiro exemplo nossa lista-> {numeros}\nSeu tipo é -> {type(numeros)}')

# Observe o poder da list comprehension

res = [numero * 10 for numero in numeros]
print(f'Neste primeiro exemplo vamos multiplicar cada elemento da lista por 10 -> {res}\nSeu tipo é -> {type(res)}')

# Exemplos observe o poder do comprehension

res = [numero / 2 for numero in numeros]
print(f'Neste primeiro exemplo vamos dividir cada elemento da lista por 2 -> {res}\nSeu tipo é -> {type(res)}')


def funcao(valor):
    """
    Função para teste do poder do comprehension
    :param valor: Parâmetro a ser passado para a funcao ->> receberá os valores vindo do iterável
    :return: Retorna o valor multiplicado por ele próprio
    """
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(f'Neste exemplo vamos  trabalhar com a função teste -> {res}\nSeu tipo é -> {type(res)}')


# Avaliando diferenças =>> list Comprehension x loop
# Loop


numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(f'Comparando List Comprehension x loop -> loop {numeros_dobrados}\nSeu tipo é {type(numeros_dobrados)}')

# Vamos refatorar o código acima para que seja menos traumático quando comparado com o uso do Comprehension
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(f'Comparando após refatorado List Comprehension x loop -> loop {numeros_dobrados}\nSeu tipo é {type(numeros_dobrados)}')


# O mesmo exemplo utilizndo list Comprehension ->> observe as duas formas veja a facilidade!!!
res = [numero * 2 for numero in numeros]
print(f'O mesmo exemplo com list Comprehension {res}')
print(f'O mesmo exemplo com list Comprehension {[numero * 2 for numero in numeros]}')


# Outros exemplos
# Exemplo 1 -> queremos colocar todos os caracteres em maiúscula
nome = 'Python para Ciência de Dados'
print(f'Exemplos de uso de list comprehension -> {[letra.upper() for letra in nome]}\nSeu tipo é -> {type([letra.upper() for letra in nome])}')

# Exemplo 2 -> queremos colocar apenas o primeiro caracter em maiúscula
amigos = ['joão', 'pedro', 'fernando', 'mariana', 'carlos']
print(f'Primeiro em maiúcula -> {[amigo.title() for amigo in amigos]}')

# Exemplo 3 -> trabablhando com range -> queremos multiplicar por 10 uma lista gerada por range
print(f'Trabalhando com range -> {[numero * 10 for numero in range(1, 10)]}')

# Exemplo 4 -> convertendo uma lista para boolean
print(f'Converte para Boolean -> {[bool(valor) for valor in [0, [],"", True, 1, 2, 3, 100.37]]}')

# Exemplo 5 -> transformando números em string usando cast
print(f'Tranformando números em strings -> {[str(letra) for letra in [1, 2, 3, 4, 5]]}')
