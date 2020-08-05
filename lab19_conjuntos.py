"""
Conjuntos => em Python conjuntos são chamados de Sets

Conjuntos em qualquer linguagem de programação, dizem respeitos à Teoria dos Conjuntos da Matemática.

Dito isto, da mesma forma que na matemática podemos escrever:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Sets (conjuntos) elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilar quando precisamos armazenar elementos, mas não nos importamos com
a ordenação deles. Quando não precisamos nos preocupar com chave, valores e itens duplicados

Os conjuntos (sets) em Python são referenciados por {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

NOTA: para conhecer todos os métodos que trabalham com Sets faça dir(sets) -> pratique

"""

# Definindo um conjunto:
# Forma 1
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}  # Observe que temos dados repetidos
print(f'Conhecendo os dados -> {s} - seu tipo é -> {type(s)}')

# OBS.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# note no print acima que os valores repetidos não foram impressos, no entanto, não foi gerado erro
# e os valores repetidos não são considerados parte do conjunto (Sets)

# Forma 2
t = set('Python para Ciência de Dados')
print(f'Conhecendo os dados -> {t} - seu tipo é -> {type(t)}')

# Note que no exemplo acima uma String foi convertida num Set e até mesmo os espaços repeitos foram descartados
# ou considerados não parte do Set

# Podemos determinar se determinado elemento está contido em um conjunto
num = 5
if num in s:
    print(f'Encontrei o {num} em s -> {s}')
else:
    print(f'Não encontrei o {num} em s -> {s}')

# É importante lemnrar que, além de não termos valores duplicados, não temos ordem em um Set

# Lista aceitam valores duplicados então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Podemos imprimir a lista -> {lista} - seu tipo é -> {type(lista)} - tamanho -> {len(lista)}')
# Tuplas aceitam valores duplicados então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Podemos imprimir a tupla -> {tupla} - seu tipo é -> {type(tupla)} - tamanho -> {len(tupla)}')
# Dicionários não aceitam valores duplicados em suas chaves então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Podemos imprimir o dicionário -> {dicionario} - seu tipo é -> {type(dicionario)} - tamanho -> {len(dicionario)}')
# Conjuntos não aceitam valores duplicados então temos 8 elementos
s = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Podemos imprimir o set -> {s} - seu tipo é {type(s)} - tamanho -> {len(s)}')

# OBS.: Dicionários não matém a ordem de geração e também não é ordenável

# Como em qualquer conjunto Python, podemos colocar tipos de dados misturados em Sets
s = {1, 'b', 'abacate', 44.22, 51}
print(f'Podemos imprimir o conjunto misturado s -> {s} - seu tipo é {type(s)} - tamanho -> {len(s)}')

# Podemos iterar em um conjunto (Sets) normalmente
for valor in s:
    print(f'O valor encontrado em s é -> {valor}')

# Usos interessantes com Sets
# Imagina que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(f'Para saber a cidade de origem dos visitantes podemos imprimir a lista -> {cidades}')
print(f'Se quisermos saber quantos visitantes passaram pela feira basta saber o tamanho da lista -> {len(cidades)}')

# Agora queremos saber quantas cidades diferentes tiveram representantes na feira
# Observe aí uma boa aplicação para Sets -> basta realizar um cast na lista observe
print(f'Podemos facilmente saber quais foram as cidades que tiveram representantes na feira -> {set(cidades)}')
print(f'Podemos facilmente saber a quantidade de cidades que tiveram representantes na feira -> {len(set(cidades))}')

# Adicionando elementos em um conjunto => use o método add()
s = {1, 2, 3}
print(f'O conjunto inicialmente criado foi s -> {s}')
s.add(4)
print(f'O conjunto s após a adição de um elemento com add(4) -> {s}')
s.add(4)    # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado

# Remover elementos em um conjunto => use o método remove() => não retorna valor algum
# Forma 1 -> usando o método .remove() -> informamos o valor a ser removido
# OBS.: Caso o valor a ser removido não seja encontrado será gerado o erro KeyError
s.remove(3)
print(f'O conjunto s após a remoção de um elemento com remove(3) -> {s}')

# Forma 2 -> uso do método .discard() => nehum valor é retornado
s.discard(2)
print(f'O conjunto s após a remoção de um elemento com discard(2) -> {s}')
# OBS.: Caso o valor a ser removido não seja encontrado nenhum erro será gerado! ATENÇÃO!!!

# Copiando um conjunto para outro ...
s = {1, 2, 3}
print(f'O conjunto s inicialmente gerado -> {s}')
# Forma 1 -> Deep Copy -> uso do método copy() => objetos independentes
novo = s.copy()
print(f'O conjunto novo cópia de s -> {novo}')
novo.add(55)
print(f'O conjunto s após alteração de novo -> {s}')
print(f'O conjunto novo após alteração -> {novo}')

# Forma 2 - Shallow Copy -> mesma referência ao objeto
print(f'O conjunto s inicialmente gerado -> {s}')
novo = s
print(f'O conjunto novo cópia Shallow de s -> {novo}')
novo.add(33)
print(f'O conjunto s após alteração de novo -> {s}')
print(f'O conjunto novo após ter sido alterado -> {novo}')

# Podemos remover todos os elementos de um conjunto com o uso do método clear()
s = {1, 2, 3}
print(f'O conjunto s inicialmente gerado -> {s}')
s.clear()
print(f'O conjunto s após uso do método clear() -> {s}')

# Métodos matemáticos de Conjuntos
# Imagine que temos dois conjuntos: um deles com estudantes do curso Python e o outro com estudantes do curso de JAVA
# NOTA: para facilitar os exemplos consideraremos nomes iguais referentes à mesma pessoa

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Observe que os conjuntos possuem tamanhos diferentes e que alguns alunos que estudam Python também estudam Java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 => utilizando union -> União da matemática dos conjuntos
unicos = estudantes_java.union(estudantes_python)
print(f'Os nomes únicos, isto o total de alunos dos cursos sem repetição é -> {unicos}')
unicos1 = estudantes_python.union(estudantes_java)
print(f'Os nomes únicos, isto o total de alunos dos cursos sem repetição é -> {unicos1}')

# NOTA: esta é uma operação que independe da ordem o resultado será o mesmo

# Forma 2 => utilizando o caractere pipe | (or)
unicos2 = estudantes_python | estudantes_java
print(f'Os nomes únicos, usando pipe | é -> {unicos2}')

# Queremos gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando intersection => intersecção da matemática

ambos1 = estudantes_python.intersection(estudantes_java)
ambos2 = estudantes_java.intersection(estudantes_python)
print(f'Intersecção a partir de python -> {ambos1}')
print(f'Intersecção a partir de java -> {ambos2}')

# Forma 2 - Utilizando o & (and)

ambos1 = estudantes_python & estudantes_java
ambos2 = estudantes_java & estudantes_python
print(f'Intersecção a partir de python -> {ambos1}')
print(f'Intersecção a partir de java -> {ambos2}')

# NOTA: não diferença o resultado será o mesmo

# Queremos agora gerar estudantes que estão em um curso, mas não estão no outro -> uso do método difference()
so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)
print(f'Só estudam python -> {so_python}')
print(f'Só estudam java -> {so_java}')


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho => * para Sets numéricos

s = {1, 2, 3, 4, 5, 6}
print(f'Os elemento do conjunot s -> {s}')
print(f'A soma dos elementos do conjunto s -> {sum(s)}')
print(f'O valor máximo dos elementos do conjunto s -> {max(s)}')
print(f'O valor mínimo dos elementos do conjunto s -> {min(s)}')
print(f'A dimensão do conjunto s -> {len(s)}')
