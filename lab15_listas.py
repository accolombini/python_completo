"""
Listas => em Python funcionam como vetores/matrizes (arrays) de outras linguagens, com a diferença de serem
DINÂMICOS e também poderem trabalhar com QUALQUER tipo de dado.
$$ DINÂMICO: não possui tamanho fixo: ou seja, podemos criar a lista e simplesmente ir adicionando elementos
$$ QUALQUER: listas não possuem tipo de dados fixo, ou seja, simplesmente você cria uma lista e adicona
qualquer tipo de dado nela. As listas em Pyton são representadas por colchetes: []

Nota: para saber mais da potencialidade de uma lista Python digite dir(lista)

"""
type([])
lista1 = [1, 90, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['D', 'i', 'a', 'd', 'o', 'A', 'b', 'a', 'c', 'a', 't', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Dia do Abacate')

# Podemos facilmente checar se determinado valor está contido na lista
num = 81
if num in lista4:
    print(f'Encontrei o número -> {num}')
    print(f'E a lista4 é formada por -> {lista4}')
else:
    print(f'Não encontrei o número -> {num}')
    print(f'E a lista4 é formada por -> {lista4}')

letra = 'i'
if letra in lista5:
    print(f'Encontrei a letra -> {letra}')
    print(f'E a lista5 é formada por -> {lista5}')
else:
    print(f'Não encontrei a letra -> {letra}')
    print(f'E a lista5 é formada por -> {lista5}')

# Podemos facilmente ordenar uma lista -> observe
print(f'Vamos ordenar a a lista1 -> {lista1}')
lista1.sort()  # Atenção o método sort() não retorna valor, por exemplo, não é válido ordena = lista1.sort()
print(f'Depois de ordenada -> {lista1}')

# Ordenando strings
print(f'Vamos ordenar a a lista5 -> {lista5}')
lista5.sort()  # Atenção o método sort() não retorna valor, por exemplo, não é válido ordena = lista5.sort()
print(f'Depois de ordenada -> {lista5}')

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(f'Na lista1 temos quantos 1? -> {lista1.count(1)}')
print(f'Na lista5 temos quantos \'a\'? -> {lista5.count("a")}')

# Adicionando elementos em listas => usaremos a função append()
# ATENÇÃO => com append() só adicionamos um elemento por vez -> sempre no final da lista
print(f'Lista1 originalmente -> {lista1}')
lista1.append(42)
print(f'Lista1 depois do append() -> {lista1}')
# Isso é um erro
# lista1.append(7, 14, 21)
# Isso é perfeitamente possível, estamos passando um único elemento do tipo lista, observe
lista1.append([7, 14, 21])  # Coloca a lista como elemento único
print(f'Lista1 depois do append() -> {lista1}')
num = [7, 14, 21]
if num in lista1:
    print(f'Encontrei a lista -> {num}')
    print(f'E a lista1 é formada por -> {lista1}')
else:
    print(f'Não encontrei a lista -> {num}')
    print(f'E a lista1 é formada por -> {lista1}')

# O método extend() faz o mesmo que o append() -> observe. Note no entanto, que os elementos serão adiconados
# individualmente -> no caso do exemplo, equivale a utilizar três vezes o método append()
# ATENÇÃO: o extend() não adiciona elemento único, por exemplo, lista1.extend(5) -> seria um erro
# NOTA: para trabalhar com extend() você precisa passar iteráveis
lista1.extend([123, 44, 47])    # Coloca cada elemento da lista como um valor adiconal
print(f'Lista1 depois do extend() -> {lista1}')
num = 123
if num in lista1:
    print(f'Encontrei a lista -> {num}')
    print(f'E a lista1 é formada por -> {lista1}')
else:
    print(f'Não encontrei a lista -> {num}')
    print(f'E a lista1 é formada por -> {lista1}')

# Podemos inserir um elemento na lista informando a posição do índice => podemos definir a posição de inserção
# Para isso devemos usar o método =>> insert()
# OBS.: isso não substitui o valor original, ele apenas será deslocado para uma posição após a inserção
lista1.insert(2, 'Novo valor')  # Estamos inserindo na posição 3 da lista a string 'Novo valor'
print(f'A lista1 após o uso do insert() fica -> {lista1}')

# Podemos facilmente juntar duas listas =>> observe a seguir
lista6 = lista1 + lista2
print(f'A lista6 resultado da junção da lista1 com a lista2 é -> {lista6}')

# Podemos ainda fazer a junção sem criar uma nova lista =>> observe
lista1 += lista2
print(f'A lista1 resultado da junção da lista1 com a lista2 é -> {lista1}')

# Observe como podemos obter o resultado assima com o extend() -> a note que não precisamos criar outra lista
lista1.extend(lista2)
print(f'A lista1 resultado do uso do extend() com a lista2 é -> {lista1}')

# Vamos retomar as listas originais
lista1 = [1, 90, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['D', 'i', 'a', 'd', 'o', 'A', 'b', 'a', 'c', 'a', 't', 'e']

# Podemos facilmente inverter uma lista utilizando o método reverse() =>> observe
print(f'A lista1 na ordem correta -> {lista1}')
print(f'A lista2 na ordem correta -> {lista2}')

lista1.reverse()
lista2.reverse()

print(f'A lista1 na ordem reversa -> {lista1}')
print(f'A lista2 na ordem reversa -> {lista2}')

# Outra forma de reverter uma lista é através do uso do slice =>> observe
lista1 = [1, 90, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['D', 'i', 'a', 'd', 'o', 'A', 'b', 'a', 'c', 'a', 't', 'e']
print(f'A lista1 na ordem reversa -> {lista1[::-1]}')
print(f'A lista2 na ordem reversa -> {lista2[::-1]}')

# Podemos facilmente copiar uma lista usando o método copy()
ista1 = [1, 90, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['D', 'i', 'a', 'd', 'o', 'A', 'b', 'a', 'c', 'a', 't', 'e']
lista6 = lista2.copy()
print(f'A lista6 cópia da lista2 é -> {lista6}')

# Podemos facilmente saber o número de elementos de uma lista => uso do método len()
print(f'O tamano da lista1 é de -> {len(lista1)} elementos')

# Podemos remover facilmente o último elemento de uma lista utilizando o método pop()
# O método pop() não apenas remove o último elemento, ele também o retorna

lista4 = list(range(11))
lista5 = list('Dia do Abacate')
print(f'Lista5 antes de remover o último elemento -> {lista5}')
ultimo = lista5.pop()
print(f'Lista5 após remover o último elemento -> {lista5}')
print(f'O elemento removido da lista5 foi -> {ultimo}')

# Podemos remover um elemento através do índice =>> especificando exatamente o que deseja remover
# Basta passarmos para o método po() a posição do elemento a ser removido
# Os elementos a direita deste índice serão deslocados
# NOTA: se não hover elemento no índice informado, teremos erro =>> IndexError
lista5 = list('Dia do Abacate')
remove = lista5.pop(2)
print(f'Lista5 após remover o elemento de indice  -> {lista5}')
print(f'O elemento removido da lista5 foi -> {remove}')

# Podemos facilmente remover todos os elementos de uma lista =>> basta utilizar o método clear()
lista5 = list('Dia do Abacate')
lista5.clear()
print(f'Observe a lista5 após o uso do método clear() -> {lista5}')

# Podemos facilmente repetir os elementos de uma lista
nova = [1, 2, 3]
print(f'Conhecendo a lista nova antes da repetição com * -> {nova}')
print(f'Repetindo os elementos de uma lista com * -> {nova * 3}')
outranova = ['Isso e incrivel']
print(f'Conhecendo a lista outranova antes da repetição com * -> {outranova}')
print(f'Repetindo os elementos de uma lista com * -> {outranova * 10}')

# Podemos facilmente converter uma string para uma lista
# Exemplo 1 =>> acompanhe o uso do método split()
# NOTA: por padrão o método split() separa os elementos da string pelo espaço em branco entre eles =>> observe
maior = 'Python para Ciencia de Dados'
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')
maior = maior.split()
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Exemplo2 =>> modificando o separador de espaço para vírgulas ->> note o que acontece com o método split()
maior = 'Python,para,Ciencia,de,Dados'
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')
maior = maior.split()
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Exemplo3 =>> modificando o separador de espaço para vírgulas ->> vamos agora dizer ao método split() que o separador
# é a vírgula e não o espaço em branco =>> acompanhe os detalhes
maior = 'Python,para,Ciencia,de,Dados'
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')
maior = maior.split(',')
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Podemos facilmente converter uma lista em uma string -> com o método
# Exemplo 1:
maior = ['Python', 'para', 'Ciencia', 'de', 'Dados']
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Na sequência vamos pegar a lista maior e colocar espaços entre cada elemento e converter em uma string
# NOTE: para isso usaremos o método .join()
maior = ' '.join(maior)
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Exemplo 2:
maior = ['Python', 'para', 'Ciencia', 'de', 'Dados']
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')
# Na sequência vamos pegar a lista maior e colocar cifrão $ entre cada elemento e converter em uma string
maior = '$'.join(maior)
print(f'A variável maior exibe os dados a seguir -> {maior} e seu tipo -> {type(maior)}')

# Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando os dados =>> observe a seguir
lista7 = [1, 2.34, True, 'Python', 'a', [1, 2, 3], 3456765432]
print(f'A variável lista7 exibe os dados a seguir -> {lista7} e seu tipo -> {type(lista7)}')

# Iterando sobre Listas
# Exemplo 1 >>= utilizando for
lista1 = [1, 90, 4, 27, 15, 22, 3, 1, 44, 42, 27]
soma = 0
for elemento in lista1:
    print(f'{elemento} ', end='')
    soma += elemento
print()  # Apenas para ir para a próxma linha
print(f'O valor de soma é -> {soma}')

# Exemplo 2 -> manipulando strings =>> fique atento o tipo de dado é importante faça alguns testes
soma = ''
lista2 = ['D', 'i', 'a', ' ', 'd', 'o', ' ', 'A', 'b', 'a', 'c', 'a', 't', 'e']
for elemento in lista2:
    print(f'{elemento} ', end='')
    soma += elemento
print()  # Apenas para ir para a próxma linha
print(f'O valor de soma é -> {soma}')

# Exemplo 3 >>= utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print(f'Adicione um produto em sua lista de compras ou digite "sair" para sair: ')
    produto = input().lower()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(f'Os produtos comprados foram -> {produto}')

# Utilizando variáveis em listas sem qualquer problema -> observe
numeros = [1, 2, 3, 4, 5]
print(f'Imprimindo nossa lista numeros -> {numeros}')
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(f'Imprimindo nossa lista numeros -> {numeros}')

# Em lista fazemos acesso aos elemento de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(f'Imprimindo cores completa -> {cores}')
print(f'Imprimindo cores por índices -> {cores[0]}')
print(f'Imprimindo cores por índices -> {cores[1]}')
print(f'Imprimindo cores por índices -> {cores[2]}')
print(f'Imprimindo cores por índices -> {cores[3]}')

# Podemos fazer acesso aos elementos de forma indexada inversa =>> pense numa lista como um "círculo" -> onde, o final
# de uma lista se liga ao seu início =>> mais fácil observar...
print(f'Imprimindo cores completa -> {cores}')
print(f'Imprimindo cores por índices inverso -> {cores[-1]}')
print(f'Imprimindo cores por índices inverso -> {cores[-2]}')
print(f'Imprimindo cores por índices inverso -> {cores[-3]}')
print(f'Imprimindo cores por índices inverso -> {cores[-4]}')

for cor in cores:
    print(f'Imprimindo cores no loop for -> {cor}')

print(f'{"-------------------------Separador------------------------------"}')
indice = 0
while indice < len(cores):
    print(f'Imprimindo cores no loop while -> {cores[indice]}')
    indice += 1

print(f'{"-------------------------Separador------------------------------"}')

coresi = cores[::-1]

for cor in coresi:
    print(f'Imprimindo cores no loop de forma inversa -> {cor}')

# Podemos facilmente gerar um índice em uma lista => usando o método enumerate() -> que gera uma lista
# contendo chave valor

cor = list(enumerate(cores))
print(f'Entendendendo o enumerate -> {cor} - {type(cor)}')

for indice, cor in enumerate(cores):
    print(f'Com enumerate temos chave -> {indice} e valor -> {cor}')

# ATENÇÃO => nem todas as coleções de Python aceitam repetição => Listas fazem parte de Coleções e aceitam repetições

rept = []
rept.append(2)
rept.append(2)
rept.append(2)
rept.append(2222)
rept.append(2222)
rept.append(2222)
print(f'A lista rept é formada por -> {rept}')

print(f'{"-------------------------Separador------------------------------"}')

# Outros métodos não tão importantes mas úteis
# Encontrar o índice de um elemento em uma lista => veja como é fácil em Python -> imagina uma lista muito grande
# Para isso basta utilizar o método index() -> acompanhe
# ATENÇÃO: caso não tenha o elemento procurado na lista será retornado um erro => ValueError
# NOTA: em casos de repetição de valores -> index() irá retornar o índice do primeiro encontrado
numeros = [5, 6, 7, 8, 9, 10, 12, 33, 55, 66, 77, 88, 8, 12, 11, 33, 7, 60, 28, 44, 33, 12, 45, 18, 33, 100]
# Em qual índice da lista está o valor 6?
print(f'Vamos encontrar o índice do número 6 -> {numeros.index(6)}')
# Em qual índice da lista está o valor 88?
print(f'Vamos encontrar o índice do número 88 -> {numeros.index(88)}')
# Em qual índice da lista está o valor 33?
print(f'Vamos encontrar o índice do número 33 -> {numeros.index(33)}')  # Retorna o índice do primeiro encontrado

# Podemos fazer buscas dentro de um range, ou seja, qual índice começar a buscar => Define-se o início da busca
# Em qual índice da lista está o valor 33 iniciando a busca em 10?
# ATENÇÃO: caso não tenha o elemento procurado na lista será retornado um erro => ValueError
print(f'Vamos encontrar o índice do número 33 iniciando em 10 -> {numeros.index(33, 10)}')  # Retorna o índice
# do primeiro encontrado

# Podemos fazer buscas dentro de um range inicio/fim - onde dinimos índice de início e de fim
# Define-se o início e o fim da busca
# Em qual índice da lista está o valor 33 iniciando a busca em 10?
# ATENÇÃO: caso não tenha o elemento procurado na lista será retornado um erro => ValueError
print(f'Vamos encontrar o índice do número 33 iniciando em 16 até 24 -> {numeros.index(33, 16, 24)}')  # Retorna o
# índice do primeiro encontrado

# Revisão de slicing => lista[inicio:fim:passo] >>= range[inicio:fim:passo]
# Trabalhando com slice de lista com paramétro 'inicio'
lista = [1, 2, 3, 4]
# Exemplo 1 - do segundo ao último => parâmetro de início
print(f'Teste slicing da lista completa -> {lista}')
print(f'Teste slicing da lista completa outra forma -> {lista[::]}')
print(f'Teste slicing do segundo elemento da lista até o último -> {lista[1:]}')

# Exemplo 2 - do último elemento => parâmetro de fim -> você define qual será o último elemento a ser impresso
print(f'Teste slicing do primeiro elemento até o segundo (não inclusive) -> {lista[:2]}')

# Exemplo 3 - trabalahndo com índices negativos
print(f'Teste slicing do usando índices negativos -> {lista[:-1]}')
print(f'Teste slicing do usando índices negativos -> {lista[:-3]}')

# Exemplo 4 - trabalhando com o passo -> definindo de quanto deverá ser incrementado o índice de acesso à lista
print(f'Teste slicing da lista completa usando passo 2 -> {lista[::2]}')
print(f'Teste slicing da lista iniciando em 1 usando passo 2 -> {lista[1::2]}')
print(f'Teste slicing da lista completa usando passo -1 -> {lista[::-1]}')
print(f'Teste slicing da lista completa terminando em 2 usando passo -1 -> {lista[:2:-1]}')
print(f'Teste slicing da lista completa iniciando em 2 usando passo -1 -> {lista[2::-1]}')

# Invertendo valores numa lista
# Exemplo 1 -> fazendo de forma manual
nomes = ['Python', 'Ciencia', 'Dados']
print(f'A lista nomes original é -> {nomes}')
nomes[0], nomes[1], nomes[2] = nomes[2], nomes[1], nomes[0]
print(f'A lista nomes invertida é -> {nomes}')

# Exemplo 2 -> utilizando Python
nomes = ['Python', 'Ciencia', 'Dados']
nomes.reverse()
print(f'A lista nomes invertida usando reverse() é -> {nomes}')

# Soma*, valor máximo*, valor mínimo*, tamanho de uma lista
# NOTA: (*) válido se os valores da lista forem numéricos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 99]
print(f'A soma dos valores da lista é -> {sum(lista)}')
print(f'O máximo valor da lista é -> {max(lista)}')
print(f'O menor valor da lista é -> {min(lista)}')
print(f'O tamanho da lista é -> {len(lista)}')

# Podemos facilmente trransformar uma lista em uma tupla visualmente a diferença será o
# uso de [] para lista e () para tuplas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 99]
print(f'A lista para teste é -> {lista[::]} - e o tipo de dado => {type(lista)}')
tupla = tuple(lista)
print(f'A tupla é -> {tupla} - e o tipo de dado => {type(tupla)}')

# Desempacotamento de listas =>> se tivermos mais elementos para serem desempacotados do que variáveis para recebê-los
# teremos ValueError <=> e vice versa >>= faça testes
# Exemplo 1: lista direta
lista = [1, 2, 3]
num1, num2, num3 = lista
print(f'Desempacotando a lista num1 => {num1}')
print(f'Desempacotando a lista num2 => {num2}')
print(f'Desempacotando a lista num3 => {num3}')

# Exemplo 2: lista reversa
num1, num2, num3 = lista[::-1]
print(f'Desempacotando a lista reversa num1 => {num1}')
print(f'Desempacotando a lista reversa num2 => {num2}')
print(f'Desempacotando a lista reversa num3 => {num3}')

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# NOTA: utilizando copy() copiamos os dados da lista original para uma nova lsta, mas elas, ficaram totalmente
# independentes, ou seja, modificando uma lista, a outra não é afetada. Em Python isso recebe o nome de Deep Copy

# Forma 1 -> Deep copy ou cópia profunda
lista = [1, 2, 3]
print(f'A lista criada para testes é -> {lista}')
nova = lista.copy()
print(f'A nova lista lista cópia de lista é nova -> {nova}')
nova.append(4)
print(f'A nova lista lista cópia de lista após o uso do append -> {nova}')
print(f'A lista original após sua cópia ter realizado um append -> {lista}')

print(f'{"-------------------------Shallow------------------------------"}')
# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
# mas após realizar modificações em uma das listas, essa modificação se reflete em asmanas as listas.
# Isso em Python é chamado de Shallow copy
# Forma 2 -> Shallow copy ou cópia de referência
lista = [1, 2, 3]
print(f'A lista criada para testes é -> {lista}')
nova = lista
print(f'A nova lista lista cópia de lista é nova -> {nova}')
nova.append(4)
print(f'A nova lista lista cópia de lista após o uso do append -> {nova}')
print(f'A lista original após sua cópia ter realizado um append -> {lista}')
lista.append(8)
print(f'A nova lista lista cópia de lista após o uso do append pela lista original -> {nova}')
print(f'A lista original após sua ela ter realizado um append -> {lista}')
