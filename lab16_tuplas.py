"""
Tuplas (tuple)
Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças:
1 - As tuplas são representadas por parênteses () => Python imprime uma tupla entre () -> não importa como foi gerada
2 - As tuplas são imutáveis => toda operação em uma tupla gera uma nova tupla

Por que utilizar tuplas?
    Tuplas são mais rápidas que listas
    Tuplas deixam seu código mais seguro -> isso porque trabalhar com dados imutáveis deixam seu código mais confiável

OBS.: métodos para adição e remoção não existem nas tuplas
NOTA: para mais informações sobre tuplas use => dir(tupla)

"""
# CUIDADO 1: As tuplas são representadas por () => observe
tupla1 = tuple(range(1, 7))
print(f'A tupla gerada é -> {tupla1} - e seu tipo pode ser confirmado -> {type(tupla1)}')

tupla2 = 1, 2, 3, 4, 5, 6
print(f'A tupla2 é -> {tupla2} - e seu tipo pode ser confirmado -> {type(tupla2)}')

# CUIDADO 2: Tuplas com um único elemento =>> ATENÇÃO isso não é uma tupla -> observe
tupla3 = (5)
print(f'A tupla3 é -> {tupla3} - e seu tipo pode ser confirmado -> {type(tupla3)}')

# CUIDADO 3: Tuplas com um único elemento =>> ATENÇÃO isso é uma tupla -> observe o uso da vírgula
tupla4 = (5, )
print(f'A tupla4 é -> {tupla4} - e seu tipo pode ser confirmado -> {type(tupla4)}')

# CONCLUSÃO: tuplas são definidas pelo uso da vírgula e não do parênteses. O parenteses é a forma como o Python
# reperesenta uma tupla
# (5) -> não é tupla
# (5,) -> é tupla
# 5, -> é tupla
tupla5 = 7,
print(f'A tupla5 é -> {tupla5} - e seu tipo pode ser confirmado -> {type(tupla5)}')

# Usando range() para gerar uma tupla -> observe o uso do cast tuple
tupla = tuple(range(11))
print(f'A tupla gerada por range é -> {tupla} - e seu tipo pode ser confirmado -> {type(tupla)}')

# Desempacotamento de Tuplas -> note que o resultado depende do tipo de dados presente na tupla
tupla = ('Python', 'Ciencia de Dados')
linguagem, aplicacao = tupla
print(f'A tupla gerada é -> {tupla} - e seu tipo pode ser confirmado -> {type(tupla)}')
print(f'A tupla desempacotada é -> {linguagem} - e seu tipo pode ser confirmado -> {type(linguagem)}')
print(f'A tupla desempacotada é -> {aplicacao} - e seu tipo pode ser confirmado -> {type(aplicacao)}')

tupla = (20, 200)
primeiro, segundo = tupla
print(f'A tupla gerada é -> {tupla} - e seu tipo pode ser confirmado -> {type(tupla)}')
print(f'A tupla desempacotada é -> {primeiro} - e seu tipo pode ser confirmado -> {type(primeiro)}')
print(f'A tupla desempacotada é -> {segundo} - e seu tipo pode ser confirmado -> {type(segundo)}')

# OBSERVAÇÃO => gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar.

# Soma*, Valor Máximo*, Valor mínimo* e tamanho => são aplicáveis à tuplas
# (*) se os valores forem inteiros ou reais
tupla = tuple(range(1, 100, 5))
print(f'A tupla gerada é -> {tupla}')
print(f'A soma dos elementos da tupla é -> {sum(tupla)}')
print(f'O valor máximo dos elementos da tupla é -> {max(tupla)}')
print(f'O valor mínimo dos elementos da tupla é -> {min(tupla)}')
print(f'A quantidade de elementos da tupla é -> {len(tupla)}')

# Concatenação de tuplas => são perfeitamente possíveis pois não estamos mudando nehuma das tuplas envolvidas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
print(f'A tupla1 gerada é -> {tupla1} - seu tipo é {type(tupla1)}')
print(f'A tupla2 gerada é -> {tupla2} - seu tipo é {type(tupla2)}')
print(f'A concatenação de tupla1 com tupla2 é -> {tupla1 + tupla2} - seu tipo é {type(tupla1 + tupla2)}')
print(f'A tupla1 após concatenação é -> {tupla1} - seu tipo é {type(tupla1)}')
print(f'A tupla2 após concatenação é -> {tupla2} - seu tipo é {type(tupla2)}')

# Podemos criar uma terceira tupla a partir de uma tupla já existente, mas nunca alterar a existente
tupla3 = tupla1 + tupla2
print(f'A tupla3 gerada é -> {tupla3} - e seu tipo é {type(tupla3)}')
print(f'A tupla1 após concatenação é -> {tupla1} - seu tipo é {type(tupla1)}')
print(f'A tupla2 após concatenação é -> {tupla2} - seu tipo é {type(tupla2)}')

# ATENÇÃO: tuplas são imutáveis, mas podemos sobrescrever seus valores -> observe
tupla1 = tupla1 + tupla2
print(f'A tupla1 após sobrever é -> {tupla1} - seu tipo é {type(tupla1)}')
print(f'A tupla2 após operação de sobrescrita é -> {tupla2} - seu tipo é {type(tupla2)}')

# Podemos verificar se um determinado elemento está presente em uma tupla => retorna True or False
print(f'O elemento "b" está presente na tupla -> {"b" in tupla1}')
print(f'O elemento 45 está presente na tupla -> {45 in tupla1}')

# Iteirando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(f'O conteudo da tupla é -> {n}')

for indice, valor in enumerate(tupla):
    print(f'O índice da tupla é -> {indice} - o valor contído na posição apontada pelo índice é -> {valor}')

# Contando elementos dentro de uma tupla => use o método count()
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b', 'a')
print(f'Contando quantos "a" estão contidos na tupla -> {tupla.count("a")}')

maior = tuple('Python para Ciência de Dados')
print(f'A tupla maior é -> {maior}')
print(f'Contando quantos "o" estão contidos na tupla -> {maior.count("o")}')

# Dicas na utilização de TUPLAS
# Devemos utilizar Tuplas sempre que não for necessário modificar os dados contidos numa coleção
# Exemplo 1:
meses = ('janeiro', 'fevereiro',  'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro')
meses_lista = ['janeiro', 'fevereiro',  'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
               'novembro', 'dezembro']
# Note que não faz sentido permitir operações na lista meses_lista -> meses_lista.append('abóbora')

# O acesso a elementos de uma tupla também é semelhante ao usado em listas
print(f'O mês mais incrível do ano é -> {meses[7].title()}')

# Iteirar utilizando while
indice = 4
while indice < len(meses):
    print(f'imprimindo os meses com while -> {meses[indice]}')
    indice += 1

# Verificando em qual índice está um determinado elemento na tupla => uso do método index()
print(f'Em qual índice está o elemento "outubro"? -> {meses.index("outubro")}')
# OBS.: caso o elemento não exista na lista será gerado erro -> ValueError

# Slicing em tuplas => tupla[inicio:fim:passo] >>= observe que usamos colchetes []
print(f'Todos os meses -> {meses[0:]}')
print(f'Todos os meses em ordem inversa -> {meses[::-1]}')
print(f'Todos os meses pares -> {meses[1::2]}')

# Copiando uma tupla para outra =>> em tuplas não temos o problema de Shallow Copy apenas Deep Copy
# Note que faz sentido não haver Shallow Copy em Tuplas, pois estas são imutáveis
tupla = (1, 2, 3)
nova = tupla
print(f'Nossa tupla original é -> {tupla}')
print(f'A cópia de tupla é nova - feita por atribuição -> {nova}')
print(f'Nossa tupla original após cópia feita por atribuição é -> {tupla}')
outra = (4, 5, 6)
nova += outra
print(f'A tupla nova adicionou o conteúdo de outra ficando -> {nova}')
print(f'Nossa tupla original após operação de concatenação -> {tupla}')

