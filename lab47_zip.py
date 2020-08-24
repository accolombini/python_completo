"""
Zip =>> zip() cria um iterável (zip object) que agrega elemento de cada um dos iteráveis passados como entrada
        em pares (é preciso que sejam pares)e seu valor de retorno é <zip object at 0x00000258F59A44C0>
        e seu tipo é <class 'zip'>.
        Podemos acessar seus valores através de um cast, mas lembre-se, fazendo isso uma vez não teremos
        mais acesso ao objeto zip.
        Podemos utilizar diferentes iteráveis com zip() ao mesmo tempo sem problemas

        OBS.:   O zip() utiliza como parâmetro o menor tamanho em iterável. isso significa que se estiver
                trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor
                iterável acabar.

"""

# Exemplos de zip() ->> note que é preciso haver pares, caso não existam serão desprezados por zip
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7]

zip1 = zip(lista1, lista2, 'abcd')
print(f'Quem é lista1 ->> {lista1}')
print(f'Quem é lista2 ->> {lista2}')
print(f'Quem é zip1() ->> {zip1}\nSeu tipo é ->> {type(zip1)}\nPodemos acessar seu valor list ->> {list(zip1)}')
print(f'Quem é zip1() ->> Podemos acessar seu valor tupla ->> {tuple(zip1)}')  # Vazio já foi usado!!!
print(f'Quem é zip1() ->> Podemos acessar seu valor set ->> {set(zip1)}')  # Vazio já foi usado!!!
zip1 = zip(lista1, lista2)
print(f'Quem é zip1() ->> Podemos acessar seu valor dict ->> {dict(zip1)}')  # Vazio já foi usado!!!

zip1 = zip(lista1, lista2, 'abcdef')
print(f'Quem é zip1() ->> Podemos acessar seu valor list ->> {list(zip1)}')
zip1 = zip(lista1, lista2, 'abcdef')
print(f'Quem é zip1() ->> Podemos acessar seu valor tupla ->> {tuple(zip1)}')  # Vazio já foi usado!!!
zip1 = zip(lista1, lista2, 'abcdef')
print(f'Quem é zip1() ->> Podemos acessar seu valor set ->> {set(zip1)}')  # Vazio já foi usado!!!
zip1 = zip(lista1, lista2)  # Note que para trabalhar com dicionários só podemos ter chave e valor
print(f'Quem é zip1() ->> Podemos acessar seu valor dict ->> {dict(zip1)}')  # Vazio já foi usado!!!

# Podemos utilizar diferentes iteráveis com zip()

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

ztudo = zip(tupla, lista, dicionario.values())

print(f'Imprimindo todo mundo \nTupla => {tupla}\nLista => {lista}\nDicionário => {dicionario.values()}')
print(f'Imprimindo zip de tudo =>> {list(ztudo)}')

ztudo = zip(tupla, lista, dicionario)  # Iteirando com as chaves do dicionário

print(f'Imprimindo todo mundo \nTupla => {tupla}\nLista => {lista}\nDicionário => {dicionario}')
print(f'Imprimindo zip de tudo =>> {list(ztudo)}')

# Podemos trabalhar com lista de tuplas ->> observe o uso do * para realizar o desempacotamento

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(f'Desempacotando com * =>> {list(zip(*dados))}')
print(f'Desempacotando com * =>> {list(zip(dados))}')  # Observe que sem o * zip() iterage [((0, 1),), ((1, 2),),...

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']
print(f'Visualizando dados de entrada\nProva1 ->> {prova1}\nProva2 ->> {prova2}\nAlunos ->> {alunos}')

# O desafio aqui é criar um dicionário com a maior nota de cada estudante

print(f'Gerando um zip() com as três entradas ->> {list(zip(alunos, prova1, prova2))}')

# Resolvendo o problema usando zip() e Comprehension
final = {dado[0].title(): max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(f'Resolvendo o desafio =>> {final}')

# Outra solução é com o uso de map() ->> observe

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
# Precisamos agora converter para dicionário
print(f'Outra solução =>> {dict(final)}')
