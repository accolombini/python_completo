"""
Filter =>> sua funçao é filtrar dados de uma determinada coleção

    - Assim como a função map(), a função filter() recebe dois parâmetros, sendo um uma função e o outro um iterável
    - Cada valor do iterável será passado para a função que deverá retornar algum valor
    - DICA: Como função trabalhe com lambdas
    - ATENÇÃO: Assim como map() a função filter() ->> tem como retorno <class 'filter'> que
    após seu uso uma vez estará VAZIA ->> Fique atento!!!
    - A diferença entre map() e filter()
        - map() => recebe dois argumentos, uma função e um iterável e retorna um objeto mapeado pela função
        e faz isso para cada elemento do iter'vel
        - filter() => recebe dois argumentos, uma função e um iterável e retorna um objeto filtrando apenas os elementos
        de acordo com a função
    NOTA: a diferença entre map() e filter() está no retorno da função que em filter() sempre retorno True ou False
"""
# Vamos fazer um import para dar suporte a este laboratório =>> Biblioteca para trabalhar com dados estatísticos

import statistics

# Exemplo 1
valores = 1, 2, 3, 4, 5, 6
print(f'Conhecendo a variável valores -> {valores}\nSeu tipo é -> {type(valores)}')
media = sum(valores) / len(valores)
print(f'A média de valores é -> {media}\nSeu tipo é -> {type(media)}')

# Nosso desafio é filtrar os dados para os valores que estão acima da média para os dados a seguir

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#  Calculando a média com a função mean() da biblioteca statistics

media = statistics.mean(dados)
# Note que o retorno de lambda é True ou False ->> sendo assim,no caso para True o valor do dado será passado para filter
res = filter(lambda valor: valor > media, dados)
print(f'Filtrando dados acima da média ->> {list(res)}\nO valor da média é -> {round(media, 2)}\n'
      f'Seu tipo é -> {type(res)}')
print(f'Filtrando dados acima da média reimprimindo ->> {list(res)}\nO valor da média é -> {round(media, 2)}\n'
      f'Seu tipo é -> {type(res)}')  # Observe que o retorno será uma lista vazia

# Uma aplicação importante de filter() é na remoção de dados faltantes

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(f'A lista completa de paises ->> {paises}')
print(f'Filtrando com lambda dados faltantes ->> {list(filter(lambda dado: dado != "", paises))}')
# Solução mais adequada =>> use None
print(f'Filtrando com tipo None dados faltantes ->> {list(filter(None, paises))}')

# Exemplo mais complexo ->> note que temos uma lista na qual cada elemento é um dicionário chave/valor

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cahorro', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

print(f'Conhecendo os dados -> {usuarios}\nSeu tipo é -> {type(usuarios)}')

# Desafio =>> filtrar usuários que estão inativos no Twitter
# Forma 1 =>> observe e perceba as diferenças
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

print(f'A relação de usuários inativos no tweeter forma 1 -> {inativos}')

# Forma 2 =>> observe e perceba as diferenças ->> repetindo os dados aqui para fins didáticos


usuarios_f2 = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cahorro', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

inativos = list(filter(lambda user: not user['tweets'], usuarios_f2))

print(f'A relação de usuários inativos no tweeter forma 2 -> {inativos}')


# Combinando filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Desafio =>> devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))

print(f'O resultado do desafio é ->> {lista}')
